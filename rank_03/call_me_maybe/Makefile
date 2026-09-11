# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.de  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/06 02:51:25 by maprunty          #+#    #+#              #
#    Updated: 2026/09/11 14:42:43 by maprunty        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



.PHONY: install run debug clean lint lint-strict build-llm

PYTHON        := python3
MAIN          := src
GOINFRE	      := $(HOME)/goinfre
CMM		      := $(GOINFRE)/cmm
UV_VENV_DIR	  := $(CMM)/venv
UV_CACHE_DIR  := $(CMM)/cache
UV            := UV_CACHE_DIR=$(UV_CACHE_DIR) UV_VENV_DIR=$(UV_VENV_DIR) uv
LLM_SDK       := ${CMM}/llm_sdk
PYREPL        := ipython --colors=Linux --automagic --no-simple-prompt
WHEEL         := $(wildcard $(LLM_SDK)/dist/*.whl)
DATA_DIR      := $(CMM)/data

run: install
	$(UV) run $(PYTHON) $(MAIN)

install: venv build-llm data
	$(UV) sync --no-dev

dev: fclean install
	$(UV) sync  --dev --reinstall-package $(LLM_SDK)


repl:
	$(UV) run $(PYREPL)


debug:
	$(PYTHON) -m pdb $(MAIN)


venv:
	mkdir -p $(UV_VENV_DIR)
	mkdir -p $(UV_CACHE_DIR)
	[ -e .venv ] || ln -s /home/maprunty/goinfre/cmm/venv .venv

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
	rm -rf $(LLM_SDK)
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


dl-llm_sdk:
	mkdir -p $(LLM_SDK)
	[ -e llm_sdk ] || ln -s $(LLM_SDK) llm_sdk
	curl -fL "https://cdn.intra.42.fr/document/document/48109/llm_sdk.zip" -o ${CMM}/llm_sdk.zip
	unzip -o ${CMM}/llm_sdk.zip -d ${CMM}

data:
	mkdir -p $(DATA_DIR)
	[ -e data ] || ln -s $(DATA_DIR)
	curl -fL "https://cdn.intra.42.fr/document/document/48108/data.zip" -o ${CMM}/data.zip
	unzip -o ${CMM}/data.zip -d ${CMM}


build-llm: dl-llm_sdk
	$(UV) build llm_sdk --wheel
