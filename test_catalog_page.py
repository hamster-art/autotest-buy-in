from page.locators import ProductPageLocators
from page.catalog_page import CatalogPage


def test_products_in_stock(browser):
    page = CatalogPage(browser, ProductPageLocators.URL)
    page.open()
    page.filter_product_in_stock()
    page.search_items_found()
    page.should_not_be_empty_message()
