import importlib.util
from pathlib import Path


ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location(
    "reset_progress",
    ROOT / "tools" / "reset_progress.py",
)
assert SPEC is not None
reset_progress = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(reset_progress)

KATAS_DIR = reset_progress.KATAS_DIR
TEMPLATES = reset_progress.TEMPLATES


def test_reset_templates_cover_every_kata_folder():
    kata_names = {
        path.name
        for path in KATAS_DIR.iterdir()
        if path.is_dir() and not path.name.startswith("__")
    }

    assert set(TEMPLATES) == kata_names


def test_reset_templates_are_practice_stubs():
    for template in TEMPLATES.values():
        assert "raise NotImplementedError" in template
