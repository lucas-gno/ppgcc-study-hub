# -*- coding: utf-8 -*-
"""
Build Phase 1 Super Lessons (Topics 01 to 08)
Applies the Einstein Principle: "Se você não consegue explicar algo para uma criança de seis anos, você mesmo não entende."
Features:
- Warm, welcoming, humanized tone ("Você")
- Micro-step cognitive blocks (word-breakdown with phonetic pronunciation)
- Formula boxes with KaTeX + integrated reading guides ("Como se fala" / "O que significa")
- Semantic rich callouts (.philosophy, .computation, .warning / .trap-box, .warshall)
- Native vector SVGs (.visual-diagram-card)
- Interactive tactile widgets (.interactive-card / widgets.js)
- In-lesson Active Retrieval quiz (4 conceptual questions with instant color-coded feedback + live score banner)
- Next Step preview card (.next-step-card)
- Primary CTA to the official question bank (../questoes.html?topico=<id>)
- 100% offline, zero emojis, zero external CDNs
"""

import html
import json
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import phase1_lesson_content
import svg_diagrams

DB_PATH = ROOT / "data" / "mestrado.db"
LESSONS_DIR = ROOT / "lessons"

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

LESSON_WIDGET_CONFIGS = {
    1: {
        "id": "lesson-widget-1",
        "init": "if (typeof initSetOperationsWidget === 'function') initSetOperationsWidget('lesson-widget-1');",
        "diagram": svg_diagrams.get_diagram_topico_1_cartesian_product(),
    },
    2: {
        "id": "lesson-widget-2",
        "init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-2', [[1,1,0],[0,0,1],[0,0,1]]);",
        "diagram": svg_diagrams.get_diagram_topico_2_digraph(),
    },
    3: {
        "id": "lesson-widget-3",
        "init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-3', [[1,1,0],[0,1,1],[0,0,1]]);",
        "diagram": svg_diagrams.get_diagram_topico_3_transitive_closure(),
    },
    4: {
        "id": "lesson-widget-4",
        "init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-4', [[1,1,0],[1,1,0],[0,0,1]]);",
        "diagram": svg_diagrams.get_diagram_topico_4_mod3_partition(),
    },
    5: {
        "id": "lesson-widget-5",
        "init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-5', [[1,0,1],[0,1,0],[1,0,1]]);",
        "diagram": svg_diagrams.get_diagram_topico_4_components(),
    },
    6: {
        "id": "lesson-widget-6",
        "init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-6', [[1,1,1],[0,1,1],[0,0,1]]);",
        "diagram": svg_diagrams.get_diagram_topico_6_divisors_24(),
    },
    7: {
        "id": "lesson-widget-7",
        "init": "if (typeof initBooleanMatrixWidget === 'function') initBooleanMatrixWidget('lesson-widget-7', [[1,1,1,1],[0,1,0,1],[0,0,1,1],[0,0,0,1]]);",
        "diagram": svg_diagrams.get_diagram_topico_7_dual_bounds(),
    },
    8: {
        "id": "lesson-widget-8",
        "init": "if (typeof initHasseReductionWidget === 'function') initHasseReductionWidget('lesson-widget-8');",
        "diagram": svg_diagrams.get_diagram_topico_8_divisors_12() + "\n" + svg_diagrams.get_diagram_topico_8_hypercube() + "\n" + svg_diagrams.get_diagram_topico_8_n5_m3(),
    },
}

EMOJI_PATTERN = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")

def sanitize_no_emojis(text: str) -> str:
    return EMOJI_PATTERN.sub("", text or "")

def build_lesson_html(tid: int, data: dict, q_count: int, total_topics: int = 8) -> str:
    wcfg = LESSON_WIDGET_CONFIGS[tid]
    slug = LESSON_SLUGS[tid]

    # Prev / Next navigation
    prev_link = (
        f'<a class="hub-btn-secondary hub-btn-sm" href="./{LESSON_SLUGS[tid - 1]}">Aula Anterior</a>'
        if tid > 1
        else '<a class="hub-btn-secondary hub-btn-sm" href="../edital.html">Voltar ao Edital</a>'
    )
    next_link = (
        f'<a class="hub-btn-secondary hub-btn-sm" href="./{LESSON_SLUGS[tid + 1]}">Próxima Aula</a>'
        if tid < total_topics
        else '<a class="hub-btn-secondary hub-btn-sm" href="../edital.html">Concluir Fase 1 no Edital</a>'
    )

    # Word breakdowns
    wb_html = []
    for wb in data.get("word_breakdowns", []):
        wb_html.append(f"""
<div class="word-breakdown">
  <div><strong class="term">{html.escape(wb['term'])}</strong> <span class="pronunciation">[{html.escape(wb['pronunciation'])}]</span></div>
  <p style="margin: 6px 0 4px; font-size: 0.92rem; color: #475569;"><strong>Origem e Conceito:</strong> {html.escape(wb['etymology'])}</p>
  <p style="margin: 0; font-size: 0.96rem; color: #0f172a;"><strong>No mundo real e computação:</strong> {html.escape(wb['plain_meaning'])}</p>
</div>
""")

    # Formulas
    formulas_html = []
    for fm in data.get("formulas", []):
        formulas_html.append(f"""
<div class="formula-box">
  <div class="math-display">$${fm['latex']}$$</div>
  <div class="reading-guide">
    <div style="font-weight:600; margin-bottom:4px; color:#78350f;">[Como se fala]: <em>"{html.escape(fm['spoken'])}"</em></div>
    <div style="color:#92400e;">[O que significa]: {html.escape(fm['meaning'])}</div>
  </div>
</div>
""")

    # Traps
    traps_html = []
    for tr in data.get("traps", []):
        traps_html.append(f"""
<div class="trap-box">
  <strong style="display:block; margin-bottom:4px;">[Cuidado com a Pegadinha da Banca]: {html.escape(tr['title'])}</strong>
  <div>{html.escape(tr['text'])}</div>
</div>
""")

    # Active Retrieval Quiz
    quiz_questions = data.get("questions", [])
    quiz_blocks = []
    js_gabarito = {}
    js_fb = {}

    for i, q in enumerate(quiz_questions, start=1):
        js_gabarito[i] = q["correct"]
        js_fb[i] = {
            "correct": q["correct_fb"],
            "incorrect": q["incorrect_fb"],
        }
        opts_html = []
        for letter in ["A", "B", "C", "D"]:
            opt_text = q["options"][letter]
            opts_html.append(
                f'<button type="button" class="option-item" onclick="submitActiveRetrieval({i}, \'{letter}\')">'
                f'<strong>{letter})</strong> {html.escape(opt_text)}'
                f'</button>'
            )

        quiz_blocks.append(f"""
<div class="question-block" id="q{i}">
  <div class="question-title"><strong>Questão de Retenção {i} de 4:</strong> {html.escape(q['question'])}</div>
  <div class="options-list">
    {''.join(opts_html)}
  </div>
  <div class="feedback-box" id="fb-{i}"></div>
</div>
""")

    quiz_section_html = f"""
<section class="quiz-section" aria-label="Active Retrieval — Retenção Imediata">
  <h2>Active Retrieval — Fixação Imediata da Aula</h2>
  <p class="hub-muted">Quatro perguntas de verificação imediata para checar se os conceitos e fórmulas se assentaram na sua mente antes de praticar na banca de concurso.</p>
  {''.join(quiz_blocks)}
  <div class="score-banner" id="score-box" style="display:none;">
    <div id="score-text"></div>
  </div>
</section>
"""

    symbol_dictionary_html = """
<div class="como-se-le" style="margin-top:2rem;">
  <div class="como-se-le-title">[Dicionário Fonético de Símbolos Lógicos]</div>
  <p>Para ler com fluência natural qualquer fórmula desta lição:</p>
  <ul style="margin-left: 1.25rem;">
    <li>$\\in$ : <em>"Pertence a"</em> (ex: $a \\in A \\to$ <em>"o elemento a pertence ao conjunto A"</em>).</li>
    <li>$\\subseteq$ : <em>"Está contido em"</em> ou <em>"é subconjunto de"</em> (ex: $R \\subseteq A \\times B \\to$ <em>"R está contido em A vezes B"</em>).</li>
    <li>$\\land$ : <em>"E"</em> (conjunção lógica, exige que ambas as condições sejam verdadeiras).</li>
    <li>$\\lor$ : <em>"OU"</em> (disjunção lógica, basta que uma seja verdadeira).</li>
    <li>$\\iff$ : <em>"Se, e somente se"</em> (equivalência lógica bidirecional).</li>
    <li>$\\implies$ : <em>"Implica que"</em> ou <em>"se... então..."</em> (condicional unidirecional).</li>
    <li>$\\forall$ : <em>"Para todo..."</em> ou <em>"Qualquer que seja..."</em> (quantificador universal).</li>
    <li>$\\exists$ : <em>"Existe ao menos um..."</em> (quantificador existencial).</li>
    <li>$\\emptyset$ : <em>"Conjunto vazio"</em> (a sacola sem nenhum elemento).</li>
  </ul>
</div>
"""

    page = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aula {tid:02d}: {html.escape(data['title'])} · PPGCC IFCE</title>
  <link rel="stylesheet" href="../assets/katex/katex.min.css">
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body class="hub-body">
  <main class="lesson-container">
    <div class="hub-page-header">
      <div>
        <div class="hub-eyebrow">Fase 1 · Tópico {tid:02d} de 37 · Tempo estimado: 45 min</div>
        <h1 class="hub-title">{html.escape(data['title'])}</h1>
        <p class="hub-subtitle">{html.escape(data['subtitle'])}</p>
      </div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <a class="hub-btn-secondary hub-btn-sm" href="../edital.html">Edital</a>
        <a class="hub-btn-primary hub-btn-sm" href="../questoes.html?topico={tid}">Questões ({q_count})</a>
      </div>
    </div>

    <!-- 1. Transição Ontológica & Filosofia -->
    <div class="callout philosophy">
      <div class="callout-title">[Filosofia da Lógica]: {html.escape(data['philosophy_title'])}</div>
      <div>{data['philosophy_text']}</div>
    </div>

    <!-- 2. Dicionário Fonético de Símbolos -->
    {symbol_dictionary_html}

    <!-- 3. Degraus Cognitivos e Desmistificação de Termos -->
    <section aria-label="Degraus Cognitivos e Termos">
      <h2>1. Degraus Cognitivos: Desmistificando os Termos</h2>
      <p>Entendendo a etimologia e o significado real antes de qualquer fórmula complexa:</p>
      {''.join(wb_html)}
    </section>

    <!-- 4. Fórmulas Limpas com Guia de Leitura -->
    <section aria-label="Fórmulas Canônicas e Como se Fala">
      <h2>2. Fórmulas Canônicas: Como se Lê e o que Significa</h2>
      <p>Cada símbolo rigoroso acompanhado de sua pronúncia fonética e tradução intuitiva para sistemas de TI:</p>
      {''.join(formulas_html)}
    </section>

    <!-- 5. Aplicação Computacional -->
    <div class="callout computation">
      <div class="callout-title">[Computação e Infraestrutura]: {html.escape(data['computation_title'])}</div>
      <div>{data['computation_text']}</div>
    </div>

    <!-- 6. Representação Visual Vetorial SVG Nativo -->
    <section aria-label="Pilar Visual — Diagrama Vetorial">
      <h2>3. Anatomia Visual: Diagrama Vetorial Nativo</h2>
      <p class="hub-muted">Inspeção espacial sem Mermaid e sem texto desformatado (ADR 0008).</p>
      {wcfg['diagram']}
    </section>

    <!-- 7. Laboratório Interativo Tátil -->
    <section aria-label="Pilar Interativo — Laboratório Tátil">
      <h2>4. Laboratório Interativo: Manipulação em Tempo Real</h2>
      <p class="hub-muted">Clique nos controles para experimentar o comportamento da estrutura e visualizar os estados.</p>
      <div class="interactive-card">
        <div id="{wcfg['id']}"></div>
      </div>
    </section>

    <!-- 8. Pegadinhas de Concurso -->
    <section aria-label="Pegadinhas da Banca">
      <h2>5. Armadilhas Clássicas da Banca Examinadora</h2>
      {''.join(traps_html)}
    </section>

    <!-- 9. Active Retrieval (Retenção Imediata da Aula) -->
    {quiz_section_html}

    <!-- 10. Card Próxima Parada -->
    <div class="next-step-card">
      <h3>Próxima Parada</h3>
      <p>{html.escape(data['next_step'])}</p>
      <div style="margin-top: 1rem;">
        {next_link}
      </div>
    </div>

    <!-- 11. Conclusão e CTA para a Banca de Questões -->
    <section class="lesson-footer-cta" aria-label="Conclusão e Prática de Questões">
      <div>
        <strong style="display:block; color:var(--text-main); margin-bottom:4px;">Prática Focada deste Tópico no Banco</strong>
        <span class="hub-muted" id="lesson-q-status">Carregando questões deste tópico no Banco...</span>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
        <button type="button" class="hub-btn-secondary" id="lesson-toggle-read-btn">Marcar aula como concluída</button>
        <a class="hub-btn-primary" href="../questoes.html?topico={tid}" id="lesson-practice-btn">Praticar questões desta aula na banca</a>
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

      {wcfg['init']}

      if (typeof renderMathInElement === 'function') {{
        renderMathInElement(document.body, {{
          delimiters: [
            {{ left: '$$', right: '$$', display: true }},
            {{ left: '$', right: '$', display: false }}
          ],
          throwOnError: false
        }});
      }}

      // --- Active Retrieval Engine ---
      const activeGabarito = {json.dumps(js_gabarito)};
      const activeExplanations = {json.dumps(js_fb)};
      const userAnswers = {{}};

      window.submitActiveRetrieval = function (qNum, opt) {{
        userAnswers[qNum] = opt;
        const block = document.getElementById('q' + qNum);
        const items = block.querySelectorAll('.option-item');
        const fb = document.getElementById('fb-' + qNum);
        const correctOpt = activeGabarito[qNum];

        items.forEach(function (btn) {{
          btn.classList.remove('correct', 'incorrect');
          const text = btn.textContent.trim();
          if (text.startsWith(opt + ')')) {{
            if (opt === correctOpt) btn.classList.add('correct');
            else btn.classList.add('incorrect');
          }}
          if (text.startsWith(correctOpt + ')')) {{
            btn.classList.add('correct');
          }}
        }});

        if (opt === correctOpt) {{
          fb.className = 'feedback-box correct';
          fb.innerHTML = '<strong>[Correto!]</strong> ' + activeExplanations[qNum].correct;
        }} else {{
          fb.className = 'feedback-box incorrect';
          fb.innerHTML = '<strong>[Incorreto]</strong> ' + activeExplanations[qNum].incorrect;
        }}

        if (window.renderMathInElement) {{
          renderMathInElement(fb, {{
            delimiters: [
              {{ left: '$$', right: '$$', display: true }},
              {{ left: '$', right: '$', display: false }}
            ],
            throwOnError: false
          }});
        }}

        updateActiveScore();
      }};

      function updateActiveScore() {{
        const keys = Object.keys(userAnswers);
        if (keys.length === 4) {{
          let hits = 0;
          for (let i = 1; i <= 4; i++) {{
            if (userAnswers[i] === activeGabarito[i]) hits++;
          }}
          const box = document.getElementById('score-box');
          const txt = document.getElementById('score-text');
          box.style.display = 'block';

          if (hits === 4) {{
            box.style.background = '#14532d';
            txt.innerHTML = '<strong>Sensacional: 4 de 4 acertos (100%)!</strong> Você absorveu perfeitamente a essência deste conceito. Seu cérebro está pronto para encarar as pegadinhas da banca!';
          }} else if (hits >= 2) {{
            box.style.background = '#1e3a8a';
            txt.innerHTML = '<strong>Bom desempenho: ' + hits + ' de 4 acertos.</strong> Revise as explicações das questões onde você hesitou para consolidar o vocabulário formal.';
          }} else {{
            box.style.background = '#7c2d12';
            txt.innerHTML = '<strong>Você acertou ' + hits + ' de 4.</strong> Leia com atenção os gabaritos comentados acima antes de seguir para o banco de questões.';
          }}
        }}
      }}

      // --- Store & Progress Integration ---
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
          statusEl.textContent = topicQs.length + ' questões disponíveis neste tópico no Banco (' + solved + ' resolvidas).';
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
    return sanitize_no_emojis(page)

def run_build():
    LESSONS_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    try:
        for tid in range(1, 9):
            data = phase1_lesson_content.ALL_PHASE1_DATA[tid]
            q_count = conn.execute("SELECT COUNT(*) FROM questoes WHERE topico_id = ?", (tid,)).fetchone()[0]
            page_content = build_lesson_html(tid, data, q_count)
            target = LESSONS_DIR / LESSON_SLUGS[tid]
            target.write_text(page_content, encoding="utf-8")
            print(f"Generated {target.name} ({len(page_content)} bytes)")
    finally:
        conn.close()

if __name__ == "__main__":
    run_build()
