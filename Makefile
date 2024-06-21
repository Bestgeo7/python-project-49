install:
	poetry install
start:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl
makelint:
	poetry run flake8 brain_games
makegame:
	poetry run brain-even
