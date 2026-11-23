import re

def is_html_block_start(line: str) -> bool:
    s = line.strip().lower()
    return any(s.startswith(f"<{tag}") for tag in ["div", "section", "figure", "svg", "table", "blockquote", "!--"])

def parse_html_block(lines: list[str], start_idx: int) -> tuple[str, int]:
    # Collect lines until all opened tags in this block are closed
    # or until an empty line if it's a standalone block
    collected = []
    i = start_idx
    tag_match = re.match(r"^<([a-zA-Z0-9]+)", lines[i].strip())
    if not tag_match:
        return lines[i], i + 1
    root_tag = tag_match.group(1).lower()
    
    depth = 0
    while i < len(lines):
        line = lines[i]
        collected.append(line)
        # count occurrences of <root_tag and </root_tag
        opens = len(re.findall(rf"<{root_tag}(?:[\s>]|$)", line, re.IGNORECASE))
        closes = len(re.findall(rf"</{root_tag}>", line, re.IGNORECASE))
        depth += (opens - closes)
        i += 1
        if depth <= 0:
            break
            
    return "\n".join(collected), i

# Test prototype
test_lines = [
    '<div class="visual-diagram-card">',
    '  <svg viewBox="0 0 100 100">',
    '    <circle cx="50" cy="50" r="40"/>',
    '  </svg>',
    '</div>',
    'Some markdown paragraph after.'
]

print("Is block start:", is_html_block_start(test_lines[0]))
block_html, next_idx = parse_html_block(test_lines, 0)
print(f"Collected block (next_idx={next_idx}):\n{block_html}")
print("Remaining:", test_lines[next_idx:])
