VENV := venv

all: venv

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	ifeq ($(OS),Windows_NT)
		python3 -m venv venv
		./venv/bin/pip install -r requirements.txt
	endif
	
run: venv
	./venv/bin/python3 piTrainer/piTrainer.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all run clean venv