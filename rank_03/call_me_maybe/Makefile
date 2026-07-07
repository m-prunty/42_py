# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.de  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06 02:51:25 by maprunty          #+#    #+#              #
#    Updated: 2026/07/07 23:58:21 by maprunty         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



.PHONY: install run debug clean lint lint-strict build-llm

PYTHON     := uv run python3
MAIN       := call_me_maybe.py
CONFIG     := config.txt
GOINFRE	   := $(HOME)/goinfre
CMM		   := $(GOINFRE)/cmm
UV_VENV_DIR	   := $(CMM)/venv
UV_CACHE_DIR	   := $(CMM)/cache	
UV := UV_CACHE_DIR=$(UV_CACHE_DIR) UV_VENV_DIR=$(UV_VENV_DIR) uv
LLM_SDK    := llm_sdk
PYREPL := ipython --colors=Linux --automagic --no-simple-prompt


install: venv build-llm
	$(UV) sync --no-dev

dev: fclean build-llm venv
	$(UV) sync  --dev --reinstall-package $(LLM_SDK)


repl:
	$(UV) run $(PYREPL) 

run:
	$(UV) run $(PYTHON) $(MAIN) 

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)


venv:
	mkdir -p $(UV_VENV_DIR)
	mkdir -p $(UV_CACHE_DIR)
	ln -s $(UV_VENV_DIR) .venv

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info"  -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "resized" -exec rm -rf {} +
	find . -type f -name "*.pyc"       -delete

fclean: clean
	rm -rf $(UV_VENV_DIR) .venv
	rm -rf $(UV_CACHE_DIR)
	rm -rf $(CMM)
	find . -type d -name ".venv" -exec rm -rf {} +
	find . -type d -name "wheels" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type f -name "*.whl" -exec rm -rf {} +
	find . -type f -name "uv.lock" -exec rm -rf {} +
	find . -type f -name "*.sw*" -exec rm -rf {} +

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . 

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

build-llm:
	rm -f *.whl
	cd $(LLM_SDK) && uv build --package llm_sdk --wheel 

