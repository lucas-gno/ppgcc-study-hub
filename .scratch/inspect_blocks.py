import sqlite3
import re

conn = sqlite3.connect('data/mestrado.db')
cursor = conn.cursor()
cursor.execute('SELECT topico_id, titulo, conteudo_markdown FROM aulas ORDER BY topico_id')
rows = cursor.fetchall()

for topico_id, titulo, md in rows:
    code_blocks = re.findall(r'```([a-zA-Z0-9_-]*)\n(.*?)```', md, re.DOTALL)
    print(f'=== TOPICO {topico_id}: {titulo} ===')
    for idx, (lang, block) in enumerate(code_blocks):
        lines = block.strip().split('\n')
        first_line = lines[0] if lines else ''
        print(f'  Block {idx+1} [lang={lang}]: {len(lines)} lines | first: {first_line[:80]}')
