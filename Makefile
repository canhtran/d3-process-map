installation:
	virtualenv --python=python2.7 .venv; \
	source .venv/bin/activate; \
	pip install -r requirements/main.txt; \

run:
	source .venv/bin/activate; \
	source scripts/initialize; \
	cd web; \
	flask run; \