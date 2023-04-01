.RECIPEPREFIX = _

# Add documentation to each target as a comment starting with '##'
# For example:
#   all: ## Build everything
#   test: ## Run the test suite
#   clean: ## Remove generated files

# Set the default target
.DEFAULT_GOAL := help

# Define phony targets
.PHONY: help

# Define the 'help' target
help:
_	@echo "Usage: make [target]"
_	@echo ""
_	@echo "Targets:"
_	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

# Define targets below this line
#######################################

install_dependencies: ## Install python dependencies
_   poetry install

deploy_google_infrastructure: ## Create google cloud resources
_   terraform init
_   terraform apply

store-prices-example:  ## Try the scrapper
_   python -m wallapop_scrapper.main "pokemon verde hoja" --store-data

upload-prices-to-storage-example: ## Try the uploader
_ python -m google_storage_prices_uploader.main 'pokemon verde hoja_2023-03-28.parquet'

upload-prices-to-big-query-from-storage-example: ## Try the uploader
_ python -m google_big_query_prices_uploader.main 'pokemon verde hoja_2023-03-28.parquet'
