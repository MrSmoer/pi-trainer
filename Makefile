VENV:= venv

all: venv
	

	
checkOS:
# echo $(BIN)
ifeq ($(OS),Windows_NT) 
    detected_OS := Windows
	BIN := Scripts
	RM = rmdir /Q /S
	CP = copy /Y
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
	BIN := bin
	RM = rm -rf
CP = cp -f

endif

venv: $(VENV)/$(BIN)/activate
	

$(VENV)/$(BIN)/activate: checkOS requirements.txt
ifeq ("$(wildcard $(VENV))", "")
	python -m venv $(VENV)
	$(VENV)/$(BIN)/pip install -r requirements.txt
else
		@echo "Skipping download because directory already exists."
endif
	
	
run: $(VENV)/$(BIN)/activate
	$(VENV)/$(BIN)/python piTrainer/piTrainer.py

clean: checkOS
	$(RM) $(VENV)
#find . -type f -name '*.pyc' -delete

activate:
	

.PHONY: all clean venv activate

