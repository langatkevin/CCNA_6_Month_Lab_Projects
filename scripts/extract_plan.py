import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DIR = BASE_DIR / 'docs' / 'reference'

text = (REFERENCE_DIR / 'study_plan.txt').read_text(encoding='utf-8')


def clean_whitespace(value: str) -> str:
    return re.sub(r'\s+', ' ', value).strip()


def normalize_block(lines):
    return '\n'.join(line.rstrip() for line in lines).strip()


month_blocks = []
month_pattern = re.compile(r"(^|\n)(Month\s+\d+:.*?)(?=\nMonth\s+\d+:|\nPost-CCNA|$)", re.S)
week_pattern = re.compile(r'(Week\s+\d+:.*?)(?=Week\s+\d+:|Month\s+\d+:|Post-CCNA|$)', re.S)

for match in month_pattern.finditer(text):
    block = match.group(2)
    block_lines = block.splitlines()
    if not block_lines:
        continue

    header_line = block_lines[0].strip()
    num_match = re.match(r'Month\s+(\d+):\s*(.*)', header_line)
    if not num_match:
        continue

    number = int(num_match.group(1))
    title_parts = [num_match.group(2).strip()]

    idx = 1
    while idx < len(block_lines):
        candidate = block_lines[idx].strip()
        if not candidate:
            idx += 1
            continue
        if candidate.startswith('Focus:') or candidate.startswith('Week '):
            break
        title_parts.append(candidate)
        idx += 1

    title = clean_whitespace(' '.join(title_parts))

    focus_lines = []
    in_focus = False
    for line in block_lines[idx:]:
        stripped = line.strip()
        if stripped.startswith('Focus:'):
            in_focus = True
            focus_lines.append(stripped[len('Focus:'):].strip())
            continue
        if in_focus:
            if stripped.startswith('Week '):
                break
            focus_lines.append(stripped)

    focus = clean_whitespace(' '.join(focus_lines)) if focus_lines else None

    weeks = []
    for wmatch in week_pattern.finditer(block):
        week_block = wmatch.group(1)
        week_lines = week_block.splitlines()
        if not week_lines:
            continue
        week_first = week_lines[0].strip()
        wheader = re.match(r'Week\s+(\d+):\s*(.*)', week_first)
        if not wheader:
            continue
        wnumber = int(wheader.group(1))
        wtitle = clean_whitespace(wheader.group(2).strip())
        wcontent = normalize_block(week_lines[1:])
        weeks.append({'number': wnumber, 'title': wtitle, 'content': wcontent})

    month_blocks.append({'number': number, 'title': title, 'focus': focus, 'weeks': weeks})

output_path = REFERENCE_DIR / 'plan_structure.json'
output_path.write_text(json.dumps(month_blocks, indent=2), encoding='utf-8')
print(f'Extracted {len(month_blocks)} months')
