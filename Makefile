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

deploy_prefect_pipeline: ## Create the deployment and run an agent to run it
_   prefect deployment build --name wallapop-prices-pipeline --work-queue zoomcamp-project --cron "0 3 * * *" prefect_pipeline.main:wallapop_prices_flow
_   prefect deployment apply wallapop_prices_flow-deployment.yaml
_   prefect agent start -p 'default-agent-pool'

store_prices_example:  ## Try the scrapper
_   python -m wallapop_scrapper.main "pokemon verde hoja" --store-data

upload_prices_to_storage_example: ## Try the storage uploader
_ python -m google_storage_prices_uploader.main 'pokemon verde hoja_2023-04-01.parquet'

upload_prices_to_big_query_from_storage_example: ## Try the big query uploader
_ python -m google_big_query_prices_uploader.main 'pokemon verde hoja_2023-04-01.parquet'

run_pipeline: ## Try the whole pipeline
_ python -m prefect_pipeline.main
