import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
IGNORE = {'.git', '__pycache__', '.pytest_cache', 'build'}
def skip(path): return bool(set(path.parts) & IGNORE)

def test_markdown_files_not_empty_or_todo_only():
    for path in ROOT.rglob('*.md'):
        if skip(path): continue
        text = path.read_text(encoding='utf-8').strip()
        assert text, f'empty markdown: {path}'
        compact = re.sub(r'[\s#`\-*|:：/._0-9A-Za-z]', '', text)
        assert not ('TODO' in text.upper() and len(compact) < 8), f'TODO-only markdown: {path}'

def test_skill_frontmatter():
    paths = []
    for base in ['antigravity/skills', 'claude-code/skills', 'codex/skills', 'chatgpt/skills']:
        paths.extend((ROOT / base).glob('*/SKILL.md'))
    for path in paths:
        text = path.read_text(encoding='utf-8')
        assert text.startswith('---\n'), f'missing frontmatter start: {path}'
        assert re.search(r'^name:\s*\S+', text, re.M), f'missing name: {path}'
        assert re.search(r'^description:\s*.+', text, re.M), f'missing description: {path}'

def test_no_zip_files():
    assert not [p for p in ROOT.rglob('*.zip') if not skip(p)]

def test_no_ds_store_files():
    assert not [p for p in ROOT.rglob('.DS_Store') if not skip(p)]

def test_skill_resources_have_enough_content():
    for base in ['antigravity/skills', 'claude-code/skills', 'codex/skills', 'chatgpt/skills']:
        for path in (ROOT / base).glob('*/resources/*.md'):
            nonblank = [line for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
            assert len(nonblank) >= 8, f'resource too thin: {path}'
