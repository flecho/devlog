.PHONY: venv
venv:
	virtualenv --no-download -p python3.6 venv

.PHONY: init
init:
	pip install -r requirements.txt
	mkdir instance

.PHONY: clean
clean:
	rm -rf venv

