"""Static HTML lesson generator from data/mestrado.db.

Follows ADR 0004 and NOTES.md:
- Zero Base + Triple Translation (.como-se-le)
- Mandatory Visual (<svg>) + Interactive (assets/widgets.js) dichotomy
- Reusable Browser Jupyter Sandbox (.notebook-cell) helper for Phases 2, 3, and 4
- Strict separation from Question Bank: ZERO inline questions inside lessons;
  footer links directly to ../questoes.html?topico=<id>
- Zero emojis, zero external CDNs (local KaTeX under ../assets/katex/)
"""

import html
import pathlib
import re
import sqlite3

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "mestrado.db"
LESSONS_DIR = ROOT / "lessons"

EMOJI_PATTERN = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")

LESSON_SLUGS = {
    1: "0001-teoria-dos-conjuntos.html",
    2: "0002-relacoes-binarias.html",
    3: "0003-propriedades-das-relacoes.html",
    4: "0004-relacoes-de-equivalencia.html",
    5: "0005-classes-e-particoes.html",
    6: "0006-relacoes-de-ordem.html",
    7: "0007-maximais-minimais-supremo-infimo.html",
    8: "0008-diagramas-de-hasse.html",
}


def sanitize_no_emojis(text: str) -> str:
    return EMOJI_PATTERN.sub("", text or "")


def render_notebook_sandbox_shell(
    notebook_id: str,
    title: str,
    kernel_label: str,
    code_snippet: str,
    inputs_html: str,
    inspector_html: str,
    stdout_initial: str = "Pronto para executar.",
) -> str:
    """Reusable Browser Jupyter Sandbox (.notebook-cell) shell for Phases 2, 3, and 4."""
    return sanitize_no_emojis(
        f"""
<section class="notebook-cell" id="{html.escape(notebook_id)}">
  <div class="notebook-topbar">
    <div class="notebook-dots" aria-hidden="true">
      <span class="notebook-dot dot-red"></span>
      <span class="notebook-dot dot-yellow"></span>
      <span class="notebook-dot dot-green"></span>
    </div>
    <div class="notebook-meta">
      <span class="notebook-title">{html.escape(title)}</span>
      <span class="notebook-kernel-badge">{html.escape(kernel_label)}</span>
    </div>
  </div>
  <div class="notebook-code-area">
    <pre><code>{html.escape(code_snippet)}</code></pre>
  </div>
  <div class="notebook-controls">
    <div class="notebook-inputs-group">
      {inputs_html}
    </div>
    <div class="notebook-btn-group">
      <button type="button" class="btn-notebook btn-notebook-run" data-nb-action="run">Executar</button>
      <button type="button" class="btn-notebook btn-notebook-step" data-nb-action="step">Passo a Passo</button>
      <button type="button" class="btn-notebook btn-notebook-reset" data-nb-action="reset">Resetar</button>
    </div>
  </div>
  <div class="notebook-output-grid">
    <div class="notebook-terminal-stdout">{html.escape(stdout_initial)}</div>
    <div class="notebook-inspector-panel">
      {inspector_html}
    </div>
  </div>
</section>
""".strip()
    )


def _format_inline(text: str, math_tokens: list[str], code_tokens: list[str]) -> str:
    # Protect inline code first
    def _save_code(m):
        idx = len(code_tokens)
        code_tokens.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"@@CODE{idx}@@"

    text = re.sub(r"`([^`]+)`", _save_code, text)

    # Protect inline math $...$
    def _save_inline_math(m):
        idx = len(math_tokens)
        math_tokens.append(m.group(0))
        return f"@@MATH{idx}@@"

    text = re.sub(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", _save_inline_math, text)

    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^\*\n]+?)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"(?<!\w)_([^_\n]+?)_(?!\w)", r"<em>\1</em>", escaped)

    for idx, tok in enumerate(math_tokens):
        escaped = escaped.replace(f"@@MATH{idx}@@", html.escape(tok))
    for idx, tok in enumerate(code_tokens):
        escaped = escaped.replace(f"@@CODE{idx}@@", tok)
    return escaped


def markdown_to_html(md_text: str) -> str:
    """Convert rich academic Markdown to clean HTML while keeping $...$ / $$...$$ untouched for KaTeX."""
    lines = md_text.replace("\r\n", "\n").split("\n")
    out = []
    i = 0
    skipped_top_h1 = False

    def inline(s: str) -> str:
        return _format_inline(s, [], [])

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            lang = stripped[3:].strip() or "text"
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            out.append(
                f'<pre class="code-block"><code class="language-{html.escape(lang)}">'
                f"{html.escape(chr(10).join(code_lines))}</code></pre>"
            )
            continue

        # Display math block $$ ... $$
        if stripped.startswith("$$"):
            if stripped.endswith("$$") and len(stripped) > 4:
                out.append(f'<div class="math-display">{html.escape(stripped)}</div>')
                i += 1
                continue
            math_lines = [line]
            i += 1
            while i < len(lines):
                math_lines.append(lines[i])
                if lines[i].strip().endswith("$$"):
                    i += 1
                    break
                i += 1
            out.append(f'<div class="math-display">{html.escape(chr(10).join(math_lines))}</div>')
            continue

        # Horizontal rule
        if re.match(r"^-{3,}$", stripped):
            out.append("<hr>")
            i += 1
            continue

        # Headings
        h_match = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if h_match:
            level = len(h_match.group(1))
            title_txt = h_match.group(2).strip()
            if level == 1 and not skipped_top_h1:
                skipped_top_h1 = True
                i += 1
                continue
            out.append(f"<h{level}>{inline(title_txt)}</h{level}>")
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            body = " ".join(bq_lines)
            body = re.sub(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CRITICAL|CAUTION)\]\s*", r"<strong>\1:</strong> ", body)
            out.append(f"<blockquote><p>{inline(body)}</p></blockquote>")
            continue

        # Markdown Pipe Table
        if "|" in stripped and i + 1 < len(lines) and re.match(r"^\|?[\s:-]+\|", lines[i + 1].strip()):
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            th_html = "".join(f"<th>{inline(h)}</th>" for h in headers)
            tb_html = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                for row in rows
            )
            out.append(
                f'<div class="table-wrapper"><table><thead><tr>{th_html}</tr></thead>'
                f"<tbody>{tb_html}</tbody></table></div>"
            )
            continue

        # Unordered or Ordered List
        if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            is_ordered = bool(re.match(r"^\d+\.\s+", stripped))
            tag = "ol" if is_ordered else "ul"
            items = []
            while i < len(lines):
                cur = lines[i].strip()
                if is_ordered and re.match(r"^\d+\.\s+", cur):
                    items.append(re.sub(r"^\d+\.\s+", "", cur))
                    i += 1
                elif not is_ordered and re.match(r"^[-*]\s+", cur):
                    items.append(re.sub(r"^[-*]\s+", "", cur))
                    i += 1
                else:
                    break
            li_html = "".join(f"<li>{inline(it)}</li>" for it in items)
            out.append(f"<{tag}>{li_html}</{tag}>")
            continue

        # Paragraph
        para_lines = []
        while i < len(lines):
            cur = lines[i].strip()
            if (
                not cur
                or cur.startswith("#")
                or cur.startswith("```")
                or cur.startswith("$$")
                or cur.startswith(">")
                or re.match(r"^-{3,}$", cur)
                or re.match(r"^[-*]\s+", cur)
                or re.match(r"^\d+\.\s+", cur)
            ):
                break
            para_lines.append(cur)
            i += 1
        out.append(f"<p>{inline(' '.join(para_lines))}</p>")

    return "\n".join(out)


PHASE1_VISUALS_AND_WIDGETS = {
    1: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>$x \\in A$:</strong> Lê-se 'x pertence ao conjunto A'. Analogia: o usuário x faz parte do grupo de permissões A.</p>"
            "<p><strong>$A \\subseteq B$:</strong> Lê-se 'A está contido em B' (todo elemento de A também está em B). <strong>$\\mathcal{P}(A)$:</strong> Conjunto das Partes — todas as combinações possíveis de subgrupos que podem ser formados com elementos de A ($2^{|A|}$ combinações).</p>"
            "<p><strong>$A \\times B = \\{(a, b) \\mid a \\in A \\land b \\in B\\}$:</strong> Lê-se 'Produto cartesiano de A por B é o conjunto dos pares ordenados (a, b) tais que a pertence a A e b pertence a B'. Analogia: um JOIN sem filtro (CROSS JOIN) entre duas tabelas no SQL.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 640 220" width="100%" height="auto" role="img" aria-label="Diagrama de Venn e Produto Cartesiano">'
            '<rect x="12" y="12" width="310" height="196" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
            '<text x="26" y="34" font-size="12" font-weight="600" fill="#334155">Diagrama de Venn: A e B</text>'
            '<circle cx="128" cy="120" r="62" fill="rgba(0,113,227,0.12)" stroke="#0071e3" stroke-width="2"/>'
            '<circle cx="204" cy="120" r="62" fill="rgba(16,185,129,0.12)" stroke="#10b981" stroke-width="2"/>'
            '<text x="92" y="124" font-size="14" font-weight="600" fill="#0f172a">1, 2</text>'
            '<text x="155" y="124" font-size="14" font-weight="700" fill="#0369a1">3, 4</text>'
            '<text x="226" y="124" font-size="14" font-weight="600" fill="#0f172a">5, 6</text>'
            '<text x="128" y="200" text-anchor="middle" font-size="11" fill="#64748b">A = {1,2,3,4}</text>'
            '<text x="212" y="200" text-anchor="middle" font-size="11" fill="#64748b">B = {3,4,5,6}</text>'
            '<rect x="342" y="12" width="286" height="196" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
            '<text x="356" y="34" font-size="12" font-weight="600" fill="#334155">Produto Cartesiano A x B (Pares Ordenados)</text>'
            '<line x1="382" y1="62" x2="604" y2="62" stroke="#cbd5e1" stroke-width="1"/>'
            '<line x1="382" y1="62" x2="382" y2="188" stroke="#cbd5e1" stroke-width="1"/>'
            '<text x="430" y="54" font-size="11" fill="#0369a1">b=x</text>'
            '<text x="515" y="54" font-size="11" fill="#0369a1">b=y</text>'
            '<text x="364" y="96" font-size="11" fill="#0071e3">a=1</text>'
            '<text x="364" y="146" font-size="11" fill="#0071e3">a=2</text>'
            '<circle cx="440" cy="92" r="5" fill="#0071e3"/><text x="452" y="96" font-size="11" fill="#0f172a">(1,x)</text>'
            '<circle cx="525" cy="92" r="5" fill="#0071e3"/><text x="537" y="96" font-size="11" fill="#0f172a">(1,y)</text>'
            '<circle cx="440" cy="142" r="5" fill="#0071e3"/><text x="452" y="146" font-size="11" fill="#0f172a">(2,x)</text>'
            '<circle cx="525" cy="142" r="5" fill="#0071e3"/><text x="537" y="146" font-size="11" fill="#0f172a">(2,y)</text>'
            '<text x="485" y="182" text-anchor="middle" font-size="11" fill="#64748b">|A x B| = |A| . |B| (Pares tem ordem!)</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-1"></div>',
        "widget_init": "if (typeof initSetOperationsWidget === 'function') initSetOperationsWidget('lesson-widget-1');",
    },
    2: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>$R \\subseteq A \\times B$:</strong> Lê-se 'R é uma relação binária de A em B'. Na prática: qualquer tabela associativa (N:N) ligando registros de A a registros de B.</p>"
            "<p><strong>$a R b$ ou $(a, b) \\in R$:</strong> Lê-se 'a está relacionado com b por R'. Contagem de prova (Q17 do Edital 53/2025): como há $|A| \\cdot |B|$ pares possíveis e cada par pode estar ligado (1) ou desligado (0), existem exatamente $2^{|A|\\cdot|B|}$ relações distintas.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 600 200" width="100%" height="auto" role="img" aria-label="Dígrafo e Matriz de Relação Binária">'
            '<defs><marker id="arr2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#0071e3"/></marker></defs>'
            '<rect x="12" y="12" width="576" height="176" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
            '<text x="28" y="34" font-size="12" font-weight="600" fill="#334155">Dígrafo da Relação R = {(1,1), (1,2), (2,3), (3,3)} em A = {1, 2, 3}</text>'
            '<path d="M 120 82 C 95 40, 145 40, 134 80" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arr2)"/>'
            '<line x1="146" y1="106" x2="262" y2="106" stroke="#0071e3" stroke-width="2" marker-end="url(#arr2)"/>'
            '<line x1="312" y1="106" x2="428" y2="106" stroke="#0071e3" stroke-width="2" marker-end="url(#arr2)"/>'
            '<path d="M 454 82 C 430 40, 480 40, 468 80" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arr2)"/>'
            '<circle cx="122" cy="106" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="122" y="111" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">1</text>'
            '<circle cx="288" cy="106" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="288" y="111" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">2</text>'
            '<circle cx="454" cy="106" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="454" y="111" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">3</text>'
            '<text x="300" y="168" text-anchor="middle" font-size="11" fill="#64748b">Setas indicam pares (origem, destino). Cada par gera 1 célula na matriz booleana.</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-2"></div>',
        "widget_init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-2', [[1,1,0],[0,0,1],[0,0,1]]);",
    },
    3: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>Reflexiva:</strong> $\\forall x \\in A,\\ (x,x) \\in R$ — 'Para todo x em A, x se relaciona consigo mesmo' (todos os nós têm laço próprio; diagonal principal da matriz toda igual a 1).</p>"
            "<p><strong>Simétrica:</strong> $(x,y) \\in R \\implies (y,x) \\in R$ — 'Toda rua tem mão dupla' (matriz igual à sua transposta).</p>"
            "<p><strong>Antissimétrica:</strong> $(x,y) \\in R \\land (y,x) \\in R \\implies x = y$ — 'Nunca existem duas setas opostas entre nós diferentes'.</p>"
            "<p><strong>Transitiva:</strong> $(x,y) \\in R \\land (y,z) \\in R \\implies (x,z) \\in R$ — 'Todo caminho de dois saltos possui um atalho direto'.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 640 180" width="100%" height="auto" role="img" aria-label="Assinaturas Visuais de Propriedades em Dígrafos">'
            '<defs><marker id="arr3" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#0071e3"/></marker></defs>'
            '<rect x="8" y="10" width="148" height="160" rx="10" fill="#f8fafc" stroke="#cbd5e1"/><text x="82" y="32" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Reflexiva</text>'
            '<path d="M 74 72 C 55 40, 109 40, 90 72" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arr3)"/>'
            '<circle cx="82" cy="90" r="16" fill="#fff" stroke="#0f172a" stroke-width="1.8"/><text x="82" y="95" text-anchor="middle" font-size="12" font-weight="600">x</text>'
            '<text x="82" y="148" text-anchor="middle" font-size="10.5" fill="#64748b">Laço em todo nó</text>'
            '<rect x="166" y="10" width="148" height="160" rx="10" fill="#f8fafc" stroke="#cbd5e1"/><text x="240" y="32" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Simétrica</text>'
            '<path d="M 210 82 Q 240 62 268 82" fill="none" stroke="#0071e3" stroke-width="2" marker-end="url(#arr3)"/>'
            '<path d="M 268 98 Q 240 118 210 98" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arr3)"/>'
            '<circle cx="202" cy="90" r="14" fill="#fff" stroke="#0f172a" stroke-width="1.8"/><text x="202" y="94" text-anchor="middle" font-size="12">x</text>'
            '<circle cx="278" cy="90" r="14" fill="#fff" stroke="#0f172a" stroke-width="1.8"/><text x="278" y="94" text-anchor="middle" font-size="12">y</text>'
            '<text x="240" y="148" text-anchor="middle" font-size="10.5" fill="#64748b">Ida obriga volta</text>'
            '<rect x="324" y="10" width="148" height="160" rx="10" fill="#f8fafc" stroke="#cbd5e1"/><text x="398" y="32" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Antissimétrica</text>'
            '<line x1="374" y1="90" x2="420" y2="90" stroke="#0071e3" stroke-width="2" marker-end="url(#arr3)"/>'
            '<circle cx="360" cy="90" r="14" fill="#fff" stroke="#0f172a" stroke-width="1.8"/><text x="360" y="94" text-anchor="middle" font-size="12">x</text>'
            '<circle cx="436" cy="90" r="14" fill="#fff" stroke="#0f172a" stroke-width="1.8"/><text x="436" y="94" text-anchor="middle" font-size="12">y</text>'
            '<text x="398" y="148" text-anchor="middle" font-size="10.5" fill="#64748b">Sem retorno entre distintos</text>'
            '<rect x="482" y="10" width="148" height="160" rx="10" fill="#f8fafc" stroke="#cbd5e1"/><text x="556" y="32" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Transitiva</text>'
            '<line x1="528" y1="74" x2="554" y2="108" stroke="#0071e3" stroke-width="1.8" marker-end="url(#arr3)"/>'
            '<line x1="558" y1="108" x2="584" y2="74" stroke="#0071e3" stroke-width="1.8" marker-end="url(#arr3)"/>'
            '<line x1="532" y1="66" x2="580" y2="66" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#arr3)"/>'
            '<circle cx="520" cy="66" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="520" y="70" text-anchor="middle" font-size="11">x</text>'
            '<circle cx="556" cy="116" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="556" y="120" text-anchor="middle" font-size="11">y</text>'
            '<circle cx="592" cy="66" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="592" y="70" text-anchor="middle" font-size="11">z</text>'
            '<text x="556" y="148" text-anchor="middle" font-size="10.5" fill="#64748b">Atalho x -> z obrigatório</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-3"></div>',
        "widget_init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-3', [[1,1,0],[0,1,1],[0,0,1]]);",
    },
    4: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>$a \\equiv b \\pmod{m} \\iff m \\mid (a - b)$:</strong> Lê-se 'a é congruente a b módulo m se, e somente se, m divide a diferença a - b'. Analogia: dois horários no relógio de 12 horas (21h e 9h) apontam para o mesmo ponteiro porque $12 \\mid (21 - 9)$.</p>"
            "<p><strong>Tríade de Equivalência:</strong> Toda relação que é simultaneamente <strong>Reflexiva + Simétrica + Transitiva</strong> funciona como um critério de agrupamento perfeito (como $|x|=|y|$ na Q18 da Prova 53/2025).</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 600 200" width="100%" height="auto" role="img" aria-label="Relógio Modular Z5 e Grupos de Equivalência">'
            '<rect x="12" y="12" width="576" height="176" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>'
            '<text x="28" y="34" font-size="12" font-weight="600" fill="#334155">Relógio Aritmético Módulo 5: Congruência como Equivalência</text>'
            '<circle cx="150" cy="112" r="58" fill="#ffffff" stroke="#0071e3" stroke-width="2"/>'
            '<text x="150" y="68" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">0 (5, 10)</text>'
            '<text x="200" y="98" text-anchor="middle" font-size="11.5" font-weight="600" fill="#334155">1 (6, 11)</text>'
            '<text x="182" y="152" text-anchor="middle" font-size="11.5" font-weight="600" fill="#334155">2 (7, 12)</text>'
            '<text x="118" y="152" text-anchor="middle" font-size="11.5" font-weight="600" fill="#334155">3 (8, 13)</text>'
            '<text x="100" y="98" text-anchor="middle" font-size="11.5" font-weight="600" fill="#334155">4 (9, 14)</text>'
            '<rect x="290" y="54" width="276" height="114" rx="10" fill="#ffffff" stroke="#e2e8f0"/>'
            '<text x="306" y="78" font-size="12" font-weight="600" fill="#0f172a">Teste da Tríade em |x| = |y| (Prova 2025 Q18):</text>'
            '<text x="306" y="102" font-size="11.5" fill="#15803d">1. Reflexiva: |x| = |x| (sempre verdadeiro)</text>'
            '<text x="306" y="124" font-size="11.5" fill="#15803d">2. Simétrica: |x|=|y| -> |y|=|x| (verdadeiro)</text>'
            '<text x="306" y="146" font-size="11.5" fill="#15803d">3. Transitiva: |x|=|y| e |y|=|z| -> |x|=|z|</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-4"></div>',
        "widget_init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-4', [[1,1,0],[1,1,0],[0,0,1]]);",
    },
    5: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>$[a]_R = \\{x \\in A \\mid (x, a) \\in R\\}$:</strong> Lê-se 'A classe de equivalência de a segundo R é o conjunto de todos os elementos x em A que são equivalentes a a'. Analogia: diretórios separados onde cada arquivo entra em exatamente uma pasta (sem sobreposição e sem arquivo órfão).</p>"
            "<p><strong>Partição $A/R$:</strong> O conjunto quociente divide $A$ em blocos não vazios, mutuamente disjuntos e cuja união recompõe $A$ inteiro.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 600 180" width="100%" height="auto" role="img" aria-label="Partição de Conjunto em Classes Disjuntas">'
            '<rect x="14" y="14" width="572" height="152" rx="12" fill="#f8fafc" stroke="#0f172a" stroke-width="1.5"/>'
            '<text x="28" y="36" font-size="12" font-weight="600" fill="#0f172a">Partição do Conjunto A = {0, 1, 2, 3, 4, 5} pela Congruência Módulo 3 (A / ~)</text>'
            '<rect x="30" y="52" width="170" height="96" rx="10" fill="#eff6ff" stroke="#0071e3" stroke-width="1.5"/>'
            '<text x="115" y="76" text-anchor="middle" font-size="12" font-weight="700" fill="#0071e3">[0]_3 (Resto 0)</text>'
            '<text x="115" y="110" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">0 , 3</text>'
            '<rect x="215" y="52" width="170" height="96" rx="10" fill="#f0fdf4" stroke="#10b981" stroke-width="1.5"/>'
            '<text x="300" y="76" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">[1]_3 (Resto 1)</text>'
            '<text x="300" y="110" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">1 , 4</text>'
            '<rect x="400" y="52" width="170" height="96" rx="10" fill="#faf5ff" stroke="#8b5cf6" stroke-width="1.5"/>'
            '<text x="485" y="76" text-anchor="middle" font-size="12" font-weight="700" fill="#6b21a8">[2]_3 (Resto 2)</text>'
            '<text x="485" y="110" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a">2 , 5</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-5"></div>',
        "widget_init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-5', [[1,0,1],[0,1,0],[1,0,1]]);",
    },
    6: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>$x \\preceq y$:</strong> Lê-se 'x precede y' ou 'x é menor ou igual a y na ordem parcial'. Diferente da equivalência (simétrica), a ordem é <strong>Reflexiva + Antissimétrica + Transitiva</strong>.</p>"
            "<p><strong>Ordem Parcial (Poset) vs. Ordem Total (Cadeia):</strong> Na ordem parcial (como pré-requisitos de disciplinas ou divisibilidade $m \\mid n$), dois elementos podem ser <em>incomparáveis</em> (ex.: 2 não divide 3 nem 3 divide 2). Na ordem total, todo par é comparável.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 600 200" width="100%" height="auto" role="img" aria-label="Ordem Parcial vs Ordem Total">'
            '<rect x="12" y="12" width="278" height="176" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>'
            '<text x="151" y="34" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Ordem Parcial (D6, |) — Tem Incomparáveis</text>'
            '<line x1="151" y1="64" x2="105" y2="108" stroke="#64748b" stroke-width="2"/>'
            '<line x1="151" y1="64" x2="197" y2="108" stroke="#64748b" stroke-width="2"/>'
            '<line x1="105" y1="108" x2="151" y2="152" stroke="#64748b" stroke-width="2"/>'
            '<line x1="197" y1="108" x2="151" y2="152" stroke="#64748b" stroke-width="2"/>'
            '<circle cx="151" cy="64" r="15" fill="#fff" stroke="#0071e3" stroke-width="2"/><text x="151" y="69" text-anchor="middle" font-size="12" font-weight="700">6</text>'
            '<circle cx="105" cy="108" r="15" fill="#fff" stroke="#0f172a" stroke-width="2"/><text x="105" y="113" text-anchor="middle" font-size="12" font-weight="700">2</text>'
            '<circle cx="197" cy="108" r="15" fill="#fff" stroke="#0f172a" stroke-width="2"/><text x="197" y="113" text-anchor="middle" font-size="12" font-weight="700">3</text>'
            '<circle cx="151" cy="152" r="15" fill="#fff" stroke="#0f172a" stroke-width="2"/><text x="151" y="157" text-anchor="middle" font-size="12" font-weight="700">1</text>'
            '<text x="151" y="179" text-anchor="middle" font-size="10.5" fill="#b45309">2 e 3 são incomparáveis</text>'
            '<rect x="310" y="12" width="278" height="176" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>'
            '<text x="449" y="34" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Ordem Total (Cadeia, &le;) — Tudo Comparável</text>'
            '<line x1="449" y1="54" x2="449" y2="164" stroke="#10b981" stroke-width="2"/>'
            '<circle cx="449" cy="56" r="13" fill="#fff" stroke="#10b981" stroke-width="2"/><text x="449" y="60" text-anchor="middle" font-size="11.5" font-weight="700">6</text>'
            '<circle cx="449" cy="92" r="13" fill="#fff" stroke="#10b981" stroke-width="2"/><text x="449" y="96" text-anchor="middle" font-size="11.5" font-weight="700">3</text>'
            '<circle cx="449" cy="128" r="13" fill="#fff" stroke="#10b981" stroke-width="2"/><text x="449" y="132" text-anchor="middle" font-size="11.5" font-weight="700">2</text>'
            '<circle cx="449" cy="164" r="13" fill="#fff" stroke="#10b981" stroke-width="2"/><text x="449" y="168" text-anchor="middle" font-size="11.5" font-weight="700">1</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-6"></div>',
        "widget_init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-6', [[1,1,1],[0,1,0],[0,0,1]]);",
    },
    7: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>Maximal vs. Máximo:</strong> Um elemento é <em>maximal</em> se ninguém está acima dele (pode haver vários topos empatados). Só existe <em>máximo</em> quando há um único topo acima de todos.</p>"
            "<p><strong>$\\sup(S)$ e $\\inf(S)$:</strong> Lê-se 'supremo de S' (a menor das cotas superiores) e 'ínfimo de S' (a maior das cotas inferiores). No reticulado de divisores $(D_n, \\mid)$, $\\sup(a,b) = \\operatorname{MMC}(a,b)$ e $\\inf(a,b) = \\operatorname{MDC}(a,b)$.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 600 210" width="100%" height="auto" role="img" aria-label="Elementos Maximais, Minimais, Supremo e Ínfimo">'
            '<rect x="12" y="12" width="576" height="186" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>'
            '<text x="28" y="34" font-size="12" font-weight="600" fill="#334155">Poset {2, 3, 4, 6} sob divisibilidade: Múltiplos Maximais/Minimais e Sem Reticulado Completo</text>'
            '<line x1="140" y1="74" x2="140" y2="144" stroke="#64748b" stroke-width="2"/>'
            '<line x1="250" y1="74" x2="140" y2="144" stroke="#64748b" stroke-width="2"/>'
            '<line x1="250" y1="74" x2="250" y2="144" stroke="#64748b" stroke-width="2"/>'
            '<circle cx="140" cy="74" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/><text x="140" y="79" text-anchor="middle" font-size="13" font-weight="700">4</text>'
            '<circle cx="250" cy="74" r="18" fill="#eff6ff" stroke="#0071e3" stroke-width="2"/><text x="250" y="79" text-anchor="middle" font-size="13" font-weight="700">6</text>'
            '<circle cx="140" cy="144" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/><text x="140" y="149" text-anchor="middle" font-size="13" font-weight="700">2</text>'
            '<circle cx="250" cy="144" r="18" fill="#f0fdf4" stroke="#10b981" stroke-width="2"/><text x="250" y="149" text-anchor="middle" font-size="13" font-weight="700">3</text>'
            '<text x="330" y="84" font-size="12" font-weight="600" fill="#0071e3">Maximais: {4, 6} (não há máximo único)</text>'
            '<text x="330" y="110" font-size="12" font-weight="600" fill="#15803d">Minimais: {2, 3} (não há mínimo único)</text>'
            '<text x="330" y="138" font-size="11.5" fill="#334155">Cotas superiores de {2,3}: apenas {6} -> sup({2,3}) = 6</text>'
            '<text x="330" y="160" font-size="11.5" fill="#b45309">Cotas inferiores de {2,3}: vazio neste conjunto</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-7"></div>',
        "widget_init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-7', [[1,1,1],[0,1,1],[0,0,1]]);",
    },
    8: {
        "como_se_le": (
            "<div class=\"como-se-le\">"
            "<strong>Tradução Tríplice (Zero Base) — Como se Lê e Analogia Prática</strong>"
            "<p><strong>$x \\lessdot y$:</strong> Lê-se 'x é coberto por y' ou 'x precede imediatamente y'. Significa que $x \\prec y$ e não existe nenhum elemento intermediário $z$ entre eles.</p>"
            "<p><strong>Regra de Leitura do Diagrama de Hasse:</strong> Remova todos os laços reflexivos, apague atalhos transitivos e oriente tudo para cima sem pontas de seta. Subir por uma aresta significa 'é menor que / divide / está contido'.</p>"
            "</div>"
        ),
        "svg_visual": (
            '<div class="diagram-container">'
            '<svg viewBox="0 0 640 210" width="100%" height="auto" role="img" aria-label="Diagramas de Hasse Notáveis: D12, M3 e N5">'
            '<rect x="10" y="10" width="200" height="190" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>'
            '<text x="110" y="30" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">D12 (Divisores de 12)</text>'
            '<line x1="110" y1="54" x2="75" y2="92" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="110" y1="54" x2="145" y2="92" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="75" y1="92" x2="75" y2="132" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="145" y1="92" x2="75" y2="132" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="145" y1="92" x2="145" y2="132" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="75" y1="132" x2="110" y2="170" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="145" y1="132" x2="110" y2="170" stroke="#64748b" stroke-width="1.8"/>'
            '<circle cx="110" cy="54" r="12" fill="#eff6ff" stroke="#0071e3" stroke-width="1.6"/><text x="110" y="58" text-anchor="middle" font-size="10.5" font-weight="700">12</text>'
            '<circle cx="75" cy="92" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="75" y="96" text-anchor="middle" font-size="10.5">4</text>'
            '<circle cx="145" cy="92" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="145" y="96" text-anchor="middle" font-size="10.5">6</text>'
            '<circle cx="75" cy="132" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="75" y="136" text-anchor="middle" font-size="10.5">2</text>'
            '<circle cx="145" cy="132" r="12" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="145" y="136" text-anchor="middle" font-size="10.5">3</text>'
            '<circle cx="110" cy="170" r="12" fill="#f0fdf4" stroke="#10b981" stroke-width="1.6"/><text x="110" y="174" text-anchor="middle" font-size="10.5" font-weight="700">1</text>'
            '<rect x="220" y="10" width="200" height="190" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>'
            '<text x="320" y="30" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Diamante M3 (Não Distributivo)</text>'
            '<line x1="320" y1="56" x2="265" y2="112" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="320" y1="56" x2="320" y2="112" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="320" y1="56" x2="375" y2="112" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="265" y1="112" x2="320" y2="168" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="320" y1="112" x2="320" y2="168" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="375" y1="112" x2="320" y2="168" stroke="#64748b" stroke-width="1.8"/>'
            '<circle cx="320" cy="56" r="11" fill="#fff" stroke="#0071e3" stroke-width="1.6"/><text x="320" y="60" text-anchor="middle" font-size="10">1</text>'
            '<circle cx="265" cy="112" r="11" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="265" y="116" text-anchor="middle" font-size="10">a</text>'
            '<circle cx="320" cy="112" r="11" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="320" y="116" text-anchor="middle" font-size="10">b</text>'
            '<circle cx="375" cy="112" r="11" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="375" y="116" text-anchor="middle" font-size="10">c</text>'
            '<circle cx="320" cy="168" r="11" fill="#fff" stroke="#10b981" stroke-width="1.6"/><text x="320" y="172" text-anchor="middle" font-size="10">0</text>'
            '<rect x="430" y="10" width="200" height="190" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>'
            '<text x="530" y="30" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Pentágono N5 (Não Modular)</text>'
            '<line x1="530" y1="56" x2="480" y2="95" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="480" y1="95" x2="480" y2="136" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="480" y1="136" x2="530" y2="168" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="530" y1="56" x2="580" y2="112" stroke="#64748b" stroke-width="1.8"/>'
            '<line x1="580" y1="112" x2="530" y2="168" stroke="#64748b" stroke-width="1.8"/>'
            '<circle cx="530" cy="56" r="11" fill="#fff" stroke="#0071e3" stroke-width="1.6"/><text x="530" y="60" text-anchor="middle" font-size="10">1</text>'
            '<circle cx="480" cy="95" r="11" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="480" y="99" text-anchor="middle" font-size="10">b</text>'
            '<circle cx="480" cy="136" r="11" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="480" y="140" text-anchor="middle" font-size="10">a</text>'
            '<circle cx="580" cy="112" r="11" fill="#fff" stroke="#0f172a" stroke-width="1.6"/><text x="580" y="116" text-anchor="middle" font-size="10">c</text>'
            '<circle cx="530" cy="168" r="11" fill="#fff" stroke="#10b981" stroke-width="1.6"/><text x="530" y="172" text-anchor="middle" font-size="10">0</text>'
            '</svg></div>'
        ),
        "widget_html": '<div id="lesson-widget-8"></div>',
        "widget_init": "if (typeof initHasseReductionWidget === 'function') initHasseReductionWidget('lesson-widget-8');",
    },
}


def generate_phase1_lessons(db_path: pathlib.Path = DB_PATH, out_dir: pathlib.Path = LESSONS_DIR) -> list[pathlib.Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    generated = []

    try:
        rows = conn.execute(
            """
            SELECT a.topico_id, a.titulo, a.conteudo_markdown, a.tempo_estimado_minutos,
                   t.fase_id, f.titulo AS fase_titulo
            FROM aulas a
            JOIN topicos_edital t ON t.id = a.topico_id
            JOIN fases_edital f ON f.id = t.fase_id
            WHERE a.topico_id BETWEEN 1 AND 8
            ORDER BY a.topico_id
            """
        ).fetchall()

        total_rows = len(rows)
        for idx, row in enumerate(rows):
            tid = int(row["topico_id"])
            slug = LESSON_SLUGS[tid]
            target = out_dir / slug
            vpack = PHASE1_VISUALS_AND_WIDGETS[tid]
            q_count = conn.execute(
                "SELECT COUNT(*) FROM questoes WHERE topico_id = ?", (tid,)
            ).fetchone()[0]

            prev_link = (
                f'<a class="hub-btn-secondary hub-btn-sm" href="./{LESSON_SLUGS[tid - 1]}">Aula Anterior</a>'
                if tid > 1
                else '<a class="hub-btn-secondary hub-btn-sm" href="../edital.html">Voltar ao Edital</a>'
            )
            next_link = (
                f'<a class="hub-btn-secondary hub-btn-sm" href="./{LESSON_SLUGS[tid + 1]}">Próxima Aula</a>'
                if idx + 1 < total_rows
                else '<a class="hub-btn-secondary hub-btn-sm" href="../edital.html">Concluir Fase 1 no Edital</a>'
            )

            body_html = markdown_to_html(sanitize_no_emojis(row["conteudo_markdown"]))
            titulo_clean = sanitize_no_emojis(row["titulo"])
            tempo_min = row["tempo_estimado_minutos"] or 45

            page_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aula {tid:02d}: {html.escape(titulo_clean)} · PPGCC IFCE</title>
  <link rel="stylesheet" href="../assets/katex/katex.min.css">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body class="hub-body">
  <main class="lesson-container">
    <div class="hub-page-header">
      <div>
        <div class="hub-eyebrow">Fase 1 · Tópico {tid:02d} de 37 · Tempo estimado: {tempo_min} min</div>
        <h1 class="hub-title">{html.escape(titulo_clean)}</h1>
        <p class="hub-subtitle">Didática Zero Base com Tradução Tríplice, Pilar Visual (SVG) e Manipulação Interativa.</p>
      </div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <a class="hub-btn-secondary hub-btn-sm" href="../edital.html">Edital</a>
        <a class="hub-btn-primary hub-btn-sm" href="../questoes.html?topico={tid}">Questões ({q_count})</a>
      </div>
    </div>

    <section aria-label="Nivelamento Zero Base">
      {vpack["como_se_le"]}
    </section>

    <section aria-label="Pilar Visual — Diagrama Vetorial">
      <h2>Representação Visual</h2>
      {vpack["svg_visual"]}
    </section>

    <section aria-label="Pilar Interativo — Laboratório Tátil">
      <h2>Laboratório Interativo</h2>
      {vpack["widget_html"]}
    </section>

    <article class="lesson-content">
      {body_html}
    </article>

    <section class="lesson-footer-cta" aria-label="Conclusão e Prática de Questões">
      <div>
        <strong style="display:block; color:var(--text-main); margin-bottom:4px;">Prática Focada deste Tópico</strong>
        <span class="hub-muted" id="lesson-q-status">Carregando questões deste tópico no Banco...</span>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
        <button type="button" class="hub-btn-secondary" id="lesson-toggle-read-btn">Marcar aula como concluída</button>
        <a class="hub-btn-primary" href="../questoes.html?topico={tid}" id="lesson-practice-btn">Praticar questões desta aula</a>
      </div>
    </section>

    <footer class="lesson-footer">
      <div class="lesson-footer-nav">
        {prev_link}
        {next_link}
      </div>
    </footer>
  </main>

  <script defer src="../assets/katex/katex.min.js"></script>
  <script defer src="../assets/katex/auto-render.min.js"></script>
  <script src="../assets/data.js"></script>
  <script src="../assets/icons.js"></script>
  <script src="../assets/store.js"></script>
  <script src="../assets/navbar.js"></script>
  <script src="../assets/widgets.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      const {{ store }} = window.PPGCCNavbar.init({{ prefix: '../', active: 'edital' }});
      const TOPICO_ID = {tid};

      {vpack["widget_init"]}

      if (typeof renderMathInElement === 'function') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{ left: '$$', right: '$$', display: true }},
            {{ left: '$', right: '$', display: false }}
          ],
          throwOnError: false
        }});
      }}

      const toggleBtn = document.getElementById('lesson-toggle-read-btn');
      const statusEl = document.getElementById('lesson-q-status');

      function syncLessonStatus() {{
        const isDone = store.isTopicRead(TOPICO_ID);
        toggleBtn.textContent = isDone ? 'Aula Concluída (Desmarcar)' : 'Marcar aula como concluída';
        toggleBtn.className = isDone ? 'hub-btn-secondary' : 'hub-btn-secondary';

        if (window.PPGCC_DATA && Array.isArray(window.PPGCC_DATA.questoes)) {{
          const topicQs = window.PPGCC_DATA.questoes.filter((q) => q.topico_id === TOPICO_ID);
          const answers = store.getState().answers || {{}};
          const solved = topicQs.filter((q) => Boolean(answers[q.id])).length;
          statusEl.textContent = topicQs.length + ' questões disponíveis neste tópico (' + solved + ' resolvidas).';
        }}
      }}

      toggleBtn.addEventListener('click', function () {{
        store.toggleTopicRead(TOPICO_ID);
        syncLessonStatus();
      }});

      syncLessonStatus();
      store.subscribe(syncLessonStatus);
    }});
  </script>
</body>
</html>
"""
            target.write_text(sanitize_no_emojis(page_html), encoding="utf-8")
            generated.append(target)

        return generated
    finally:
        conn.close()


if __name__ == "__main__":
    files = generate_phase1_lessons()
    print(f"Generated {len(files)} lessons in {LESSONS_DIR}")
