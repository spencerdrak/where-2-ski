dev-setup:
	if ! [ -d ".venv" ]; then echo "Virtualenv does not exist. Creating..."; virtualenv .venv --python=3.11; fi;
	poetry env use .venv/bin/python;
	poetry install;