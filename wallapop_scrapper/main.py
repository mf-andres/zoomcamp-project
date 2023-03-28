from datetime import date
from urllib.parse import quote_plus

import typer
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def search_item_prices_in_wallapop(keyword: str, headless: bool = False, store_data: bool = False):
    browser = init_browser(headless)
    url = create_request_url(keyword)
    browser.get(url)  # loads page
    click_on_accept_cookies(browser)
    wait_for_prices_to_load(browser)
    prices = get_prices(browser)
    store_prices(keyword, prices) if store_data else ""
    browser.quit()


def init_browser(headless: bool):
    options = webdriver.ChromeOptions()
    options.add_argument('headless') if headless else ""
    browser = webdriver.Chrome(options=options)
    return browser


def create_request_url(keyword):
    # Define the request url
    base_url = 'https://es.wallapop.com/app/search'
    params = {
        'keywords': quote_plus(keyword),
        'condition': 'as_good_as_new,good,new',
        'filters_source': 'quick_filters',
    }
    url = f'{base_url}?{"&".join([f"{k}={v}" for k, v in params.items()])}'
    return url


def click_on_accept_cookies(browser):
    cookies_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
    )
    cookies_button.click()


def wait_for_prices_to_load(browser):
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'ItemCard__price')]"))
    )


def get_prices(browser):
    prices = browser.find_elements(By.XPATH, "//span[contains(@class, 'ItemCard__price ItemCard__price--bold')]")
    prices = [price.text.strip().replace('€', '').replace(',', '.') for price in prices]
    print(f"prices: {prices}")
    return prices


def store_prices(keyword, prices):
    today = date.today()

    # Store the prices in a Pandas DataFrame and save to a parquet file
    df = pd.DataFrame({'price': prices})
    # df['link'].astype(str)
    # df['title'].astype(str)
    df['price'].astype(float)
    # df['date'].astype(date)
    df.to_parquet(f'{keyword}_{today.isoformat()}.parquet')


if __name__ == '__main__':
    typer.run(search_item_prices_in_wallapop)
