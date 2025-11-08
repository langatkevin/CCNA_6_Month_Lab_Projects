import json
import re
import unicodedata
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PLAN_PATH = BASE_DIR / 'docs' / 'reference' / 'plan_structure.json'
OUTPUT = BASE_DIR / 'docs' / 'roadmaps' / 'monthly-roadmap.md'

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


def main():
    plan = json.loads(PLAN_PATH.read_text())
    lines = [
        '# CCNA 6-Month Lab Roadmap',
        '',
        'This summary mirrors the reference study plan and points to the working folders under labs/.'
    ]

    for month in plan:
        month_slug = f"month-{month['number']:02d}-{slugify(month['title'])}"
        lines.append('')
        lines.append(f"## Month {month['number']:02d} - {to_ascii(month['title'])}")
        focus = to_ascii(month.get('focus', '')).strip()
        if focus:
            lines.append(f"**Focus:** {focus}")
        lines.append('')
        lines.append('| Week | Theme | Folder |')
        lines.append('| --- | --- | --- |')
        for week in month['weeks']:
            week_slug = f"week-{week['number']:02d}-{slugify(week['title'])}"
            lines.append(
                f"| {week['number']:02d} | {to_ascii(week['title'])} | labs/{month_slug}/{week_slug} |"
            )
    OUTPUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Wrote {OUTPUT}')


if __name__ == '__main__':
    main()
