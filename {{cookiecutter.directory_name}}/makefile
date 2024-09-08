.PHONY: init docs live-docs clean

init:
	mkdir -p data models
	cp .env.template .env
	if ! command -v uv &> /dev/null; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	fi
	uv sync
	if ! command -v pre-commit &> /dev/null; then \
    uv tool install pre-commit
	fi
	pre-commit install

docs:
	quarto render docs/index.qmd --to html

live-docs:
	quarto preview docs/blog-post.qmd --to html --port 7777 --no-browser

clean:
	rm -rf models/*
	rm -rf output/*
	rm -rf wandb/*
	rm -rf docs/.quarto docs/*.html
	rm -rf src/*.egg-info
