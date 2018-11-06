.PHONY: venv
venv:
	virtualenv -p python3.7 venv

.PHONY: init
init:
	pip install -r requirements.txt
	mkdir instance

.PHONY: clean
clean:
	rm -rf venv
	rm -rf instance

