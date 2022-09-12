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
ifeq ($(detected_OS), Windows)
		python -m venv $(VENV)
		$(VENV)/$(BIN)/pip install -r requirements.txt
else @echo Dont need venv, because Linux is used
endif
	
else
		@echo "Skipping download because directory already exists. Or Linux is used"
endif
	
	
run: $(VENV)/$(BIN)/activate
ifeq ($(detected_OS), Windows)
	$(VENV)/$(BIN)/python piTrainer/piTrainer.py
else
	python piTrainer/piTrainer.py
	endif

clean: checkOS
	$(RM) $(VENV)
#find . -type f -name '*.pyc' -delete

activate:
	
install:


.PHONY: all clean venv activate install uninstall

