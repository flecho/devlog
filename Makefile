.PHONY: venv
venv:
	virtualenv --no-download venv

.PHONY: init
init:
	pip install -r requirements.txt
	mkdir instance

.PHONY: clean
clean:
	rm -rf venv

