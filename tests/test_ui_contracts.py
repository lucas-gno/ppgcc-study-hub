import pathlib
import re
import subprocess
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parent.parent
EMOJI_PATTERN = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")
CDN_ASSET_PATTERN = re.compile(r"<(?:script|link)\b[^>]*(?:src|href)=[\"']https?://", re.IGNORECASE)

EXPECTED_LESSONS = {
    1: "lessons/0001-teoria-dos-conjuntos.html",
    2: "lessons/0002-relacoes-binarias.html",
    3: "lessons/0003-propriedades-das-relacoes.html",
    4: "lessons/0004-relacoes-de-equivalencia.html",
    5: "lessons/0005-classes-e-particoes.html",
    6: "lessons/0006-relacoes-de-ordem.html",
    7: "lessons/0007-maximais-minimais-supremo-infimo.html",
    8: "lessons/0008-diagramas-de-hasse.html",
}


def assert_clean_static_asset(test_case: unittest.TestCase, path: pathlib.Path):
    test_case.assertTrue(path.exists(), f"Missing file: {path}")
    content = path.read_text(encoding="utf-8")
    emojis = EMOJI_PATTERN.findall(content)
    test_case.assertEqual(emojis, [], f"Emojis found in {path.name}: {emojis}")
    cdn_hits = CDN_ASSET_PATTERN.findall(content)
    test_case.assertEqual(cdn_hits, [], f"External CDN script/link found in {path.name}: {cdn_hits}")
    return content


class UiContractsTests(unittest.TestCase):
    def test_shared_assets_have_zero_emojis(self):
        for rel in [
            "assets/icons.js",
            "assets/store.js",
            "assets/navbar.js",
            "assets/widgets.js",
            "assets/style.css",
        ]:
            assert_clean_static_asset(self, ROOT / rel)

    def test_index_page_contract(self):
        html = assert_clean_static_asset(self, ROOT / "index.html")
        for script in ["./assets/data.js", "./assets/icons.js", "./assets/store.js", "./assets/navbar.js"]:
            self.assertIn(script, html)
        self.assertIn("questoes.html", html)

    def test_edital_page_contract(self):
        html = assert_clean_static_asset(self, ROOT / "edital.html")
        for script in ["./assets/data.js", "./assets/icons.js", "./assets/store.js", "./assets/navbar.js"]:
            self.assertIn(script, html)
        self.assertIn("questoes.html?topico=", html)
        self.assertIn("toggleTopicRead", html)
        self.assertIn("obras", html)

    def test_generate_lessons_fase1_contracts(self):
        gen_script = ROOT / "scripts" / "generate_lessons.py"
        self.assertTrue(gen_script.exists(), "Missing scripts/generate_lessons.py")

        res = subprocess.run(
            ["python", str(gen_script)],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        self.assertEqual(res.returncode, 0, msg=res.stderr)

        for topico_id, rel_path in EXPECTED_LESSONS.items():
            html = assert_clean_static_asset(self, ROOT / rel_path)
            # Pilar Visual: native SVG
            self.assertIn("<svg", html, f"{rel_path} missing native SVG")
            # Pilar Interativo: widgets.js mount + init*Widget
            self.assertIn("../assets/widgets.js", html)
            self.assertRegex(html, r"init\w+Widget\(", f"{rel_path} missing interactive widget initializer")
            # Zero Base: .como-se-le
            self.assertIn("como-se-le", html, f"{rel_path} missing Zero Base como-se-le box")
            # Local KaTeX offline
            self.assertIn("../assets/katex/katex.min.css", html)
            self.assertIn("../assets/katex/katex.min.js", html)
            self.assertIn("../assets/katex/auto-render.min.js", html)
            # Strict separation: ZERO inline questions inside lessons
            self.assertNotIn("question-card", html, f"{rel_path} must NOT contain inline questions")
            self.assertNotIn("option-btn", html, f"{rel_path} must NOT contain inline option buttons")
            self.assertNotIn("initQuiz(", html, f"{rel_path} must NOT initialize inline quiz")
            # Deep-link to Question Bank & Store completion
            self.assertIn(f"../questoes.html?topico={topico_id}", html)
            self.assertIn("toggleTopicRead", html)

    def test_notebook_sandbox_shell_template_contract(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        try:
            import generate_lessons
        finally:
            sys.path.pop(0)

        shell = generate_lessons.render_notebook_sandbox_shell(
            notebook_id="nb-sample",
            title="C99 Memory Trace",
            kernel_label="Kernel Simulado C99",
            code_snippet="int x = 10;",
            inputs_html='<label>x <input type="number" value="10"></label>',
            inspector_html='<table class="notebook-memory-table"></table>',
        )
        self.assertEqual(EMOJI_PATTERN.findall(shell), [])
        for cls in [
            "notebook-cell",
            "notebook-topbar",
            "notebook-inputs-group",
            "notebook-terminal-stdout",
            "notebook-inspector-panel",
        ]:
            self.assertIn(cls, shell)

    def test_questoes_page_contract(self):
        html = assert_clean_static_asset(self, ROOT / "questoes.html")
        for asset in [
            "./assets/katex/katex.min.css",
            "./assets/katex/katex.min.js",
            "./assets/katex/auto-render.min.js",
            "./assets/data.js",
            "./assets/icons.js",
            "./assets/store.js",
            "./assets/navbar.js",
        ]:
            self.assertIn(asset, html)
        self.assertIn("parseQueryFilters", html)
        self.assertIn("normalizeOptions", html)
        self.assertIn("rateFsrsCard", html)
        self.assertIn("filterQuestions", html)


if __name__ == "__main__":
    unittest.main()
