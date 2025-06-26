# Define variables
PYTHON := python3
PYTEST := pytest
PIP := pip3
CRAWL_FILENAME := ecommerce_crawled_urls.json
PROJECT_NAME := web crawling using Python

.PHONY: install
install:
	$(PIP) install -r requirements.txt
	@echo "Installation complete"

.PHONY: test
test:
    export NODE_ENV = test

.PHONY: test
crawl-ecommerce-playground:
	- $(PYTHON) main_crawler.py --filename $(CRAWL_FILENAME)

scrap-ecommerce-playground:
	- $(PYTHON) scraper/ecommerce_scraper.py --filename $(CRAWL_FILENAME)

.PHONY: clean
clean:
    # This helped: https://gist.github.com/hbsdev/a17deea814bc10197285
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Clean Succeded"

.PHONY: distclean
distclean: clean
	rm -rf venv

.PHONY: help
help:
	@echo ""
	@echo "install : Install project dependencies"
	@echo "clean : Clean up temp files"
	@echo "crawl-ecommerce-playground : Crawl LambdaTest E-Commerce Playground"
	@echo "scrap-ecommerce-playground : Scrap the crawled output"