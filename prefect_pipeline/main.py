from prefect import task, flow
from prefect.task_runners import SequentialTaskRunner

from google_big_query_prices_uploader.main import upload_prices_to_big_query_from_storage
from google_storage_prices_uploader.main import upload_prices_to_storage
from settings.settings import Settings
from utils.path_utils import get_project_root
from wallapop_scrapper.main import search_item_prices_in_wallapop


def get_product_names():
    settings = Settings(_env_file=get_project_root() / ".env")
    return settings.keywords


@task
def search_item_prices_in_wallapop_t(product_name, headless, store_data):
    prices_file, prices = search_item_prices_in_wallapop(product_name, headless, store_data)
    return prices_file


@task
def upload_prices_to_storage_t(prices_file: str):
    upload_prices_to_storage(prices_file)


@task
def upload_prices_to_big_query_from_storage_t(prices_file: str):
    upload_prices_to_big_query_from_storage(prices_file)


@flow
def wallapop_prices_flow(name="wallapop-prices-pipeline"):
    product_names = get_product_names()

    for product_name in product_names:
        prices_file = search_item_prices_in_wallapop_t(product_name, headless=True, store_data=True)
        upload_prices_to_storage_t(prices_file)
        upload_prices_to_big_query_from_storage_t(prices_file)

wallapop_prices_flow()