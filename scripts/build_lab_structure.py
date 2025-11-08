import json
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REFERENCE_DIR = BASE_DIR / 'docs' / 'reference'
LABS_DIR = BASE_DIR / 'labs'

REPLACEMENTS = {
    '’': "'",
    '‘': "'",
    '“': '"',
    '”': '"',
    '–': '-',
    '—': '-'
}


def to_ascii(text: str) -> str:
    value = text or ''
    for bad, good in REPLACEMENTS.items():
        value = value.replace(bad, good)
    normalized = unicodedata.normalize('NFKD', value)
    return normalized.encode('ascii', 'ignore').decode('ascii')


def slugify(text: str) -> str:
    ascii_text = to_ascii(text).lower()
    slug = re.sub(r'[^a-z0-9]+', '-', ascii_text)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug or 'untitled'


def parse_week_sections(content: str):
    objectives = []
    labs = []
    milestones = []

    collecting_objectives = False

    current_section = None

    for raw_line in (content or '').splitlines():
        ascii_line = to_ascii(raw_line.strip())
        if not ascii_line:
            continue
        normalized = ascii_line.lstrip('- ').strip()
        lower = normalized.lower()

        if lower.startswith('objectives'):
            collecting_objectives = True
            continue

        if collecting_objectives and (
            lower.startswith('resources')
            or lower.startswith('hands-on')
            or lower.startswith('hands on')
            or lower.startswith('lab ')
        ):
            collecting_objectives = False
            current_section = None

        if collecting_objectives and normalized and not normalized.isdigit():
            objectives.append(normalized)
            current_section = 'Objectives'
            continue

        if lower.startswith('lab '):
            labs.append(normalized)
            current_section = 'Labs'
            continue

        if lower.startswith('(mini-project') or lower.startswith('(project') or lower.startswith('project '):
            labs.append(normalized)
            current_section = 'Labs'
            continue

        if lower.startswith('milestones & checkpoints'):
            current_section = None
            continue

        if lower.startswith('milestone') or lower.startswith('checkpoint'):
            milestones.append(normalized)
            current_section = 'Milestones'
            continue

        if lower.startswith('quizzes') or lower.startswith('time allocation') or lower.startswith('videos') or lower.startswith('books') or lower.startswith('online courses') or lower.startswith('motivation') or lower.startswith('take a short break'):
            current_section = None
            continue

        if current_section == 'Labs' and labs:
            labs[-1] = f"{labs[-1]} {normalized}"
            continue
        if current_section == 'Milestones' and milestones:
            milestones[-1] = f"{milestones[-1]} {normalized}"
            continue
        if current_section == 'Objectives' and objectives:
            objectives[-1] = f"{objectives[-1]} {normalized}"
            continue

    def dedupe(seq):
        merged = []
        for item in seq:
            clean_item = ' '.join(item.split())
            if not clean_item or clean_item.isdigit():
                continue
            if merged and not clean_item.lower().startswith('(mini-project') and not clean_item.lower().startswith('(project ') and (clean_item[0].islower() or clean_item[0] in '([' or clean_item[0].isdigit()):
                merged[-1] = f"{merged[-1]} {clean_item}"
            else:
                merged.append(clean_item)

        result = []
        seen = set()
        for item in merged:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    return {
        'Objectives': dedupe(objectives),
        'Labs': dedupe(labs),
        'Milestones': dedupe(milestones)
    }

def markdown_list(items):
    if not items:
        return '- Add your own items from the study plan.'
    return '\n'.join(f"- {item}" for item in items)


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def main():
    plan = json.loads((REFERENCE_DIR / 'plan_structure.json').read_text())
    for month in plan:
        month_slug = f"month-{month['number']:02d}-{slugify(month['title'])}"
        month_dir = LABS_DIR / month_slug
        ensure_dir(month_dir)
        focus_text = to_ascii(month.get('focus', '')).strip()
        month_lines = [f"# Month {month['number']:02d} - {to_ascii(month['title'])}"]
        if focus_text:
            month_lines.append(f"\n**Focus:** {focus_text}\n")
        month_lines.append('| Week | Theme | Folder |')
        month_lines.append('| --- | --- | --- |')
        for week in month['weeks']:
            week_slug = f"week-{week['number']:02d}-{slugify(week['title'])}"
            week_dir = month_dir / week_slug
            ensure_dir(week_dir)
            sections = parse_week_sections(week['content'])
            week_readme = [f"# Week {week['number']:02d} - {to_ascii(week['title'])}"]
            week_readme.append('')
            week_readme.append('> Adapted from the "6-Month CCNA 200-301 Study Plan" reference.')
            week_readme.append('')
            week_readme.append('## Objectives')
            week_readme.append(markdown_list(sections['Objectives']))
            week_readme.append('')
            week_readme.append('## Hands-On Labs & Mini Projects')
            week_readme.append(markdown_list(sections['Labs']))
            week_readme.append('')
            week_readme.append('## Milestones & Checkpoints')
            week_readme.append(markdown_list(sections['Milestones']))
            week_readme.append('')
            week_readme.append('## Lab Log')
            week_readme.append('| Date | Lab / Config | Key Takeaways | Evidence (files/screens) |')
            week_readme.append('| --- | --- | --- | --- |')
            week_readme.append('|  |  |  |  |')
            (week_dir / 'README.md').write_text('\n'.join(week_readme) + '\n', encoding='utf-8')
            month_lines.append(f"| {week['number']:02d} | {to_ascii(week['title'])} | [ {week_slug} ](./{week_slug}) |")
        (month_dir / 'README.md').write_text('\n'.join(month_lines) + '\n', encoding='utf-8')

    print('Generated lab directory structure under', LABS_DIR)


if __name__ == '__main__':
    main()
