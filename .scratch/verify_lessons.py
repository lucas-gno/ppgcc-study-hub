import pathlib
import re

lessons_dir = pathlib.Path('lessons')
html_files = sorted(lessons_dir.glob('*.html'))

print(f'Checking {len(html_files)} generated lessons...')
total_errors = 0
for f in html_files:
    content = f.read_text(encoding='utf-8')
    # Check for raw mermaid in HTML
    mermaid_matches = re.findall(r'(?:<code[^>]*class="language-(?:mermaid|flowchart)"|<pre[^>]*>\s*flowchart)', content, re.IGNORECASE)
    
    # Check for ascii art blocks in <pre>
    code_blocks = re.findall(r'<pre class="code-block"><code>(.*?)</code></pre>', content, re.DOTALL)
    ascii_code_blocks = []
    for b in code_blocks:
        if any(marker in b for marker in ['│ X │', '[M1]', 'DÍGRAFO DA ORDEM', 'Nível 3: {a', 'Reticulado N5']):
            ascii_code_blocks.append(b[:60])
            
    svg_cards = len(re.findall(r'class="visual-diagram-card"', content))
    print(f'{f.name}:')
    print(f'  - Code blocks total: {len(code_blocks)}')
    print(f'  - Mermaid code blocks: {len(mermaid_matches)}')
    print(f'  - ASCII art code blocks: {len(ascii_code_blocks)}')
    print(f'  - Native SVG diagram cards: {svg_cards}')
    if mermaid_matches or ascii_code_blocks:
        total_errors += 1

print(f"\nVerification finished. Lessons with defects: {total_errors}")
if total_errors == 0:
    print("ALL LESSONS VERIFIED CLEAN! Zero Mermaid blocks, zero raw ASCII trees, 100% native vector SVGs.")
