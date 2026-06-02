.PHONY: test test-solutions reset-progress

test:
	uv run pytest

test-solutions:
	uv run pytest

reset-progress:
	python3 tools/reset_progress.py
