import json
import pathlib
import subprocess
import unittest


ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_JS = ROOT / "assets" / "data.js"
OFFICIAL_KEY_53_2025 = [
    "B", "B", "C", "B", "B", "C", "E", "A", "A", "D",
    "B", "C", "C", "A", "C", "B", "D", "B", "B", "C",
]


class DataPipelineTests(unittest.TestCase):
    def test_import_and_export_generates_valid_offline_ppgcc_data(self):
        res_import = subprocess.run(
            ["python", str(ROOT / "scripts" / "import_official_2025.py")],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        self.assertEqual(res_import.returncode, 0, msg=res_import.stderr)

        # Idempotent re-run must keep count exact
        res_import_2 = subprocess.run(
            ["python", str(ROOT / "scripts" / "import_official_2025.py")],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        self.assertEqual(res_import_2.returncode, 0, msg=res_import_2.stderr)

        res_export = subprocess.run(
            ["python", str(ROOT / "scripts" / "export_db.py")],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        self.assertEqual(res_export.returncode, 0, msg=res_export.stderr)
        self.assertTrue(DATA_JS.exists(), "assets/data.js was not generated")

        # Parse assets/data.js using Node to verify syntax and inspect exported payload
        node_probe = (
            "const fs=require('fs'),vm=require('vm');"
            "const ctx={window:{}};"
            "vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),ctx);"
            "console.log(JSON.stringify(ctx.window.PPGCC_DATA));"
        )
        res_node = subprocess.run(
            ["node", "-e", node_probe, str(DATA_JS)],
            capture_output=True,
            text=True,
            cwd=str(ROOT),
        )
        self.assertEqual(res_node.returncode, 0, msg=res_node.stderr)
        data = json.loads(res_node.stdout)

        # Official structure checks
        self.assertEqual(len(data["fases"]), 5)
        self.assertEqual(len(data["topicos"]), 37)
        self.assertEqual(len(data["obras"]), 7)
        self.assertGreaterEqual(len(data["questoes"]), 64)

        # Official calendar checks (Edital 43/2026 + Retificacao 01 & 02)
        meta = data["meta"]
        self.assertEqual(meta["prova_escrita_data"], "2026-12-04")
        self.assertEqual(meta["prova_escrita_duracao_min"], 120)
        self.assertEqual(meta["arguicao_inicio"], "2026-12-14")
        self.assertEqual(meta["arguicao_fim"], "2026-12-18")
        self.assertEqual(meta["arguicao_duracao_min"], 20)

        # Exact 20 official questions of Prova 53/2025 in order 1..20
        prova_2025 = [q for q in data["questoes"] if q.get("origem") == "PROVA_53_2025"]
        self.assertEqual(len(prova_2025), 20)
        prova_2025_sorted = sorted(prova_2025, key=lambda q: q["numero_prova"])
        self.assertEqual(
            [q["numero_prova"] for q in prova_2025_sorted],
            list(range(1, 21)),
        )
        self.assertEqual(
            [q["correta"] for q in prova_2025_sorted],
            OFFICIAL_KEY_53_2025,
        )

        # Mix of 4-option (Q1-Q4, Q16-Q20) and 5-option (Q5-Q15) questions
        for q in prova_2025_sorted:
            num = q["numero_prova"]
            if num in (1, 2, 3, 4, 16, 17, 18, 19, 20):
                self.assertEqual((q.get("alt_e") or "").strip(), "", f"Q{num} should have 4 options")
            else:
                self.assertTrue((q.get("alt_e") or "").strip(), f"Q{num} should have 5 options")

        # Phase 1 topics 1..8 have lesson_file mapped
        fase1_topics = [t for t in data["topicos"] if t["fase_id"] == 1]
        self.assertEqual(len(fase1_topics), 8)
        for t in fase1_topics:
            self.assertTrue(t["lesson_file"].startswith("lessons/000"), t)


if __name__ == "__main__":
    unittest.main()
