"""
Migration script: Replace all broken Mermaid and raw ASCII diagrams in Phase 1 lessons (data/mestrado.db)
with pristine native SVG vector components wrapped in .visual-diagram-card containers.
"""

import re
import sqlite3
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import scripts.svg_diagrams as sd

DB_PATH = ROOT / "data" / "mestrado.db"


def migrate_phase1():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # TOPICO 1
    t1_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 1").fetchone()["conteudo_markdown"]
    t1_new = re.sub(r"```mermaid\s+flowchart LR\s+subgraph Dominio_A.*?```", sd.get_diagram_topico_1_cartesian_product(), t1_md, flags=re.DOTALL)
    if t1_new != t1_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 1", (t1_new,))
        print("Topico 1 migrated successfully.")
    else:
        print("Topico 1 pattern not matched or already migrated.")

    # TOPICO 2
    t2_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 2").fetchone()["conteudo_markdown"]
    t2_new = re.sub(r"```mermaid\s+flowchart LR\s+1\(\(1\)\).*?```", sd.get_diagram_topico_2_digraph(), t2_md, flags=re.DOTALL)
    if t2_new != t2_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 2", (t2_new,))
        print("Topico 2 migrated successfully.")
    else:
        print("Topico 2 pattern not matched or already migrated.")

    # TOPICO 3
    t3_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 3").fetchone()["conteudo_markdown"]
    t3_new = re.sub(r"```mermaid\s+flowchart LR.*?3\s*```", sd.get_diagram_topico_3_transitive_closure(), t3_md, flags=re.DOTALL)
    if t3_new != t3_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 3", (t3_new,))
        print("Topico 3 migrated successfully.")
    else:
        print("Topico 3 pattern not matched or already migrated.")

    # TOPICO 4
    t4_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 4").fetchone()["conteudo_markdown"]
    t4_new = re.sub(r"```\s*Grafo Não-Direcionado G:.*?Componente 3:.*?```", sd.get_diagram_topico_4_components(), t4_md, flags=re.DOTALL)
    t4_new = re.sub(r"```mermaid\s+flowchart TD\s+subgraph Particao.*?```", sd.get_diagram_topico_4_mod3_partition(), t4_new, flags=re.DOTALL)
    if t4_new != t4_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 4", (t4_new,))
        print("Topico 4 migrated successfully.")
    else:
        print("Topico 4 pattern not matched or already migrated.")

    # TOPICO 5
    t5_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 5").fetchone()["conteudo_markdown"]
    t5_new = re.sub(r"```mermaid\s+graph TD\s+subgraph \"Universo A\".*?```", sd.get_diagram_topico_5_projection(), t5_md, flags=re.DOTALL)
    if t5_new != t5_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 5", (t5_new,))
        print("Topico 5 migrated successfully.")
    else:
        print("Topico 5 pattern not matched or already migrated.")

    # TOPICO 6
    t6_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 6").fetchone()["conteudo_markdown"]
    t6_new = re.sub(r"```text\s+\{a, b, c\}\s+<-\s+Nível 3.*?\{\}\s+<-\s+Nível 0.*?```", sd.get_diagram_topico_6_hypercube(), t6_md, flags=re.DOTALL)
    t6_new = re.sub(r"```text\s+24\s+/.*?1 -----\+\s*```", sd.get_diagram_topico_6_divisors_24(), t6_new, flags=re.DOTALL)
    if t6_new != t6_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 6", (t6_new,))
        print("Topico 6 migrated successfully.")
    else:
        print("Topico 6 pattern not matched or already migrated.")

    # TOPICO 7
    t7_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 7").fetchone()["conteudo_markdown"]
    t7_new = re.sub(r"```text\s+\[8\]\s+\[12\]\s+\[18\].*?\[3\]\s+<-- Elementos Minimais.*?```", sd.get_diagram_topico_7_no_bounds(), t7_md, flags=re.DOTALL)
    t7_new = re.sub(r"```text\s+\[e\]\s+\[f\].*?\[a\]\s+\[b\]\s+<-- Elementos Minimais\s*```", sd.get_diagram_topico_7_dual_bounds(), t7_new, flags=re.DOTALL)
    if t7_new != t7_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 7", (t7_new,))
        print("Topico 7 migrated successfully.")
    else:
        print("Topico 7 pattern not matched or already migrated.")

    # TOPICO 8
    t8_md = cursor.execute("SELECT conteudo_markdown FROM aulas WHERE topico_id = 8").fetchone()["conteudo_markdown"]
    t8_new = re.sub(r"```\s*DÍGRAFO DA ORDEM \(P, <=\).*?DIAGRAMA DE HASSE\s*```", sd.get_diagram_topico_8_algorithm(), t8_md, flags=re.DOTALL)
    t8_new = re.sub(r"```\s*\[M1\]\s+\[M2\].*?\[⊥\]\s+<-- Mínimo único.*?```", sd.get_diagram_topico_8_extremals(), t8_new, flags=re.DOTALL)
    t8_new = re.sub(r"```\s*Nível 3: \{a, b, c\}\s+\(Top ⊤\).*?Nível 0: ∅\s+\(Bottom ⊥\)\s*```", sd.get_diagram_topico_8_hypercube(), t8_new, flags=re.DOTALL)
    t8_new = re.sub(r"```\s*12\s+\(Top ⊤\).*?1\s+\(Bottom ⊥\)\s*```", sd.get_diagram_topico_8_divisors_12(), t8_new, flags=re.DOTALL)
    t8_new = re.sub(r"```\s*⊤\s+/ \\\s+c\s+d\s+│ X │\s+a\s+b\s+\\ /\s+⊥\s*```", sd.get_diagram_topico_8_cross_lattice(), t8_new, flags=re.DOTALL)
    t8_new = re.sub(r"```\s*Reticulado N5 \(Pentágono\).*?0\s+0\s*```", sd.get_diagram_topico_8_n5_m3(), t8_new, flags=re.DOTALL)
    if t8_new != t8_md:
        cursor.execute("UPDATE aulas SET conteudo_markdown = ? WHERE topico_id = 8", (t8_new,))
        print("Topico 8 migrated successfully.")
    else:
        print("Topico 8 pattern not matched or already migrated.")

    conn.commit()
    conn.close()
    print("Migration finished.")


if __name__ == "__main__":
    migrate_phase1()
