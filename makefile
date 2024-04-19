.PHONY: init env docs live-docs clean

PIP := $(shell command -v uv > /dev/null && echo "uv pip" || echo "pip")

init:
	mkdir -p data models
	cp .env.template .env
	$(CONDA_EXE) env create -f env.yml
	$(CONDA_EXE) run -n NAME $(PIP) install -r requirements.txt
	$(CONDA_EXE) run -n NAME pre-commit install

env:
	$(PIP) freeze > requirements.txt

docs:
	quarto render docs/blog-post.qmd --to html

live-docs:
	quarto preview docs/blog-post.qmd --to html --port 7777 --no-browser

clean:
	rm -rf models/*
	rm -rf output/*
	rm -rf wandb/*
	rm -rf docs/.quarto docs/*.html
