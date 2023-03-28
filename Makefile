.RECIPEPREFIX = _

install_dependencies
_   poetry install

store-prices-example:
_   python -m wallapop_scrapper.main "pokemon verde hoja"

deploy_google_infrastructure:
_   terraform init
-   terraform apply
