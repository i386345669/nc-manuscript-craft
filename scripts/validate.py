#!/usr/bin/env python3
"""Validate package structure and public-facing text; not scientific meaning."""
from pathlib import Path
import argparse
import csv
import json
import re
import sys


def validate(root: Path) -> dict:
    skill = root / 'skills' / 'nc-manuscript-craft'
    errors = []
    required = ['README.md', 'README.zh-CN.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
                'FINAL_PROMPT_ZH.md', 'docs/EVALUATION.md', 'docs/SCOPE_AND_IMPROVEMENTS.md',
                'skills/nc-manuscript-craft/SKILL.md',
                'skills/nc-manuscript-craft/agents/openai.yaml',
                'skills/nc-manuscript-craft/LICENSE',
                'skills/nc-manuscript-craft/THIRD_PARTY_NOTICES.md']
    for name in required:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')
    if errors:
        return {'status': 'FAIL', 'errors': errors}
    entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\r?\n(.*?)\r?\n---\r?\n', entry, re.S)
    if not front:
        errors.append('SKILL.md has no YAML frontmatter')
    else:
        for field in ['name', 'description']:
            value = re.search(rf'^{field}:\s*(.+)$', front[1], re.M)
            if not value or not value[1].strip():
                errors.append(f'Missing skill field: {field}')
        if not re.search(r'^name:\s*nc-manuscript-craft\s*$', front[1], re.M):
            errors.append('Skill name and directory differ')
    ui = (skill / 'agents/openai.yaml').read_text(encoding='utf-8')
    if '$nc-manuscript-craft' not in ui:
        errors.append('UI default prompt does not name the skill')
    if (root / 'FINAL_PROMPT_ZH.md').read_bytes() != (skill / 'references/22-full-paper-prompt.md').read_bytes():
        errors.append('Standalone prompt and installable copy differ')
    for name in ['LICENSE', 'THIRD_PARTY_NOTICES.md']:
        if (root / name).read_bytes() != (skill / name).read_bytes():
            errors.append(f'Installable attribution copy differs: {name}')
    references = sorted((skill / 'references').glob('*.md'))
    for p in references:
        if f'references/{p.name}' not in entry:
            errors.append(f'Unrouted reference: {p.name}')
    public_patterns = {
        'private thread URL': r'codex://threads/[0-9a-f-]{20,}',
        'absolute personal path': r'(?i)(?:[A-Z]:[\\/](?:Users|Documents)[\\/]|/Users/[^/\s]+/|/home/[^/\s]+/)',
        'private source marker': r'\bT[1-9]-[MR]\d{3}\b',
        'private key material': r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',
        'GitHub token pattern': r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,})\b',
    }
    docs = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts
            and p.suffix.lower() in ['.md', '.yaml', '.yml', '.csv', '.json']]
    local_links = 0
    for p in docs:
        text = p.read_text(encoding='utf-8')
        relative = p.relative_to(root).as_posix()
        for label, pattern in public_patterns.items():
            if re.search(pattern, text):
                errors.append(f'{relative}: {label}')
        if p.suffix == '.md':
            if len(re.findall(r'^```', text, re.M)) % 2:
                errors.append(f'{relative}: unbalanced code fences')
            for match in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', text):
                target = match[1].split('#')[0]
                if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                local_links += 1
                dest = (p.parent / target).resolve()
                if not dest.is_relative_to(root.resolve()) or not dest.exists():
                    errors.append(f'{relative}: unresolved local link {target}')
    for p in (skill / 'assets').glob('*.csv'):
        with p.open(encoding='utf-8', newline='') as f:
            rows = list(csv.reader(f))
        if not rows or len(rows[0]) != len(set(rows[0])):
            errors.append(f'{p.name}: empty or duplicate CSV fields')
        if any(len(r) != len(rows[0]) for r in rows[1:]):
            errors.append(f'{p.name}: inconsistent CSV columns')
    prompt_ids = []
    for p in references:
        prompt_ids.extend(re.findall(r'^#{1,6}\s+(P\d{2}-[A-Z])\b', p.read_text(encoding='utf-8'), re.M))
    if len(prompt_ids) != len(set(prompt_ids)):
        errors.append('Repeated numbered prompt IDs')
    language = (skill / 'assets/task-brief.yaml').read_text(encoding='utf-8')
    if 'output_language: infer_from_request' not in language:
        errors.append('Task brief forces a language instead of inferring the request')
    return {'status': 'FAIL' if errors else 'PASS', 'reference_modules': len(references),
            'numbered_prompts': len(prompt_ids), 'standalone_characters': len((root / 'FINAL_PROMPT_ZH.md').read_text(encoding='utf-8')),
            'text_files_checked': len(docs), 'local_links_checked': local_links,
            'errors': errors, 'limitations': ['No scientific or semantic correctness proof',
                                             'Pattern scans do not replace human public-content review']}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = validate(args.root.resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
