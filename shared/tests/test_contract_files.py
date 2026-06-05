from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[2]

def test_contract_files_exist():
    for name in ['qz_structured_data_contract.md','qz_core_report_contract.md','qz_topic_report_contract.md']:
        path = ROOT / 'shared' / 'contracts' / name
        assert path.is_file(), f'missing {path}'
        assert path.stat().st_size > 100, f'too small {path}'

def test_sample_files_exist():
    samples = [ROOT / 'antigravity/skills/qz-reader/examples/qz_structured_data.sample.md', ROOT / 'antigravity/skills/qz-core/examples/core_report.sample.md', ROOT / 'shared/examples/qz_structured_data.example.md', ROOT / 'shared/examples/qz_core_report.example.md', ROOT / 'shared/examples/qz_full_report.example.md']
    for path in samples:
        assert path.is_file(), f'missing sample {path}'
        assert path.stat().st_size > 100, f'too small sample {path}'

def test_pdf_text_build_output_exists():
    text_dir = ROOT / 'build/pdf_text'
    index = text_dir / 'index.json'
    assert index.is_file(), 'missing build/pdf_text/index.json'
    data = json.loads(index.read_text(encoding='utf-8'))
    assert data.get('pages', 0) >= 400, 'PDF extraction index reports too few pages'
    assert len(list(text_dir.glob('page_*.txt'))) >= 400, 'PDF page text files are incomplete'
