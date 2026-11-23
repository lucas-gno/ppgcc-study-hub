import sqlite3
import re

conn = sqlite3.connect('data/mestrado.db')
cursor = conn.cursor()
cursor.execute('SELECT topico_id, titulo, conteudo_markdown FROM aulas ORDER BY topico_id')
rows = cursor.fetchall()

with open('.scratch/all_blocks_detail.txt', 'w', encoding='utf-8') as f:
    for topico_id, titulo, md in rows:
        f.write(f"\n=======================================================\n")
        f.write(f"TOPICO {topico_id}: {titulo}\n")
        f.write(f"=======================================================\n")
        code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\n(.*?)```', md, re.DOTALL)
        for idx, (lang, block) in enumerate(code_blocks):
            f.write(f"\n--- BLOCK {idx+1} [lang='{lang}'] ---\n")
            f.write(block)
            f.write("\n")

print("Exported all blocks to .scratch/all_blocks_detail.txt")
