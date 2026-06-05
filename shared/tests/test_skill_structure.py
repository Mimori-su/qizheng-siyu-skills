from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SKILLS = ['qz-study','qz-reader','qz-core','qz-love','qz-wealth','qz-health','qz-career','qz-children','qz-lawsuit','qz-election','qz-rectifier','qz-report']

SKILL_BASES = ['antigravity/skills', 'claude-code/skills', 'codex/skills', 'chatgpt/skills']

def test_12_skills_exist_in_all_skill_trees():
    for base in SKILL_BASES:
        for skill in SKILLS:
            path = ROOT / base / skill
            assert path.is_dir(), f'missing {path}'
            assert (path / 'SKILL.md').is_file(), f'missing SKILL.md for {path}'

def test_skill_resources_are_present():
    for base in SKILL_BASES:
        for skill in SKILLS:
            resources = ROOT / base / skill / 'resources'
            assert resources.is_dir(), f'missing resources for {skill}'
            assert any(p.is_file() and p.stat().st_size > 20 for p in resources.rglob('*')), f'empty resources for {skill}'

def test_platform_adapter_files_exist():
    required = [
        ROOT / 'codex/README.md',
        ROOT / 'chatgpt/README.md',
        ROOT / 'chatgpt/custom-gpt-instructions.md',
        ROOT / 'chatgpt/knowledge-files.md',
        ROOT / 'chatgpt/skills-upload-manifest.md',
        ROOT / 'cursor/README.md',
        ROOT / '.cursor/rules/qz-router.mdc',
        ROOT / '.cursor/rules/qz-data-contract.mdc',
        ROOT / '.cursor/rules/qz-safety.mdc',
        ROOT / '.cursor/rules/qz-platform-files.mdc',
        ROOT / 'claude-code/CLAUDE.md',
    ]
    for path in required:
        assert path.is_file(), f'missing platform adapter file: {path}'
        assert path.stat().st_size > 100, f'too small platform adapter file: {path}'
    assert len(list((ROOT / 'claude-code/.claude/commands').glob('qz-*.md'))) == 12
