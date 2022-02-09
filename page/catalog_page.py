import time
from page.base_page import BasePage
from .locators import ProductPageLocators


class CatalogPage(BasePage):
    def filter_product_in_stock(self):
        checkbox_in_stock = self.browser.find_element(*ProductPageLocators.CHECKBOX_IN_STOCK)
        checkbox_in_stock.click()
        assert self.is_elements_disappeared(*ProductPageLocators.LBL_IN_STOCK), \
            "Products are not in stock, but should be"

    def filter_product_on_sale(self):
        checkbox_on_sale = self.browser.find_element(*ProductPageLocators.CHECKBOX_ON_SALE)
        checkbox_on_sale.click()
        assert self.is_elements_present(*ProductPageLocators.LBL_ON_SALE), \
            "Products are not on sale, but should be"

    def should_be_empty_message(self):
        assert self.is_present(*ProductPageLocators.SEARCH_EMPTY_NOTICE), \
            "Search empty notice is not present, but should be"

    def should_not_be_empty_message(self):
        assert self.is_not_present(*ProductPageLocators.SEARCH_EMPTY_NOTICE), \
            "Search empty notice is present, but should not be"

    def search_items_not_found(self):
        search_input = self.browser.find_element(*ProductPageLocators.SEARCH_INPUT)
        search_btn = self.browser.find_element(*ProductPageLocators.SEARCH_BTN)
        search_input.send_keys(ProductPageLocators.SEARCH_NOT_SUCCESS_TEXT)
        search_btn.click()
        assert self.is_elements_disappeared(*ProductPageLocators.PRODUCT_NAME), \
            "Searched list is not empty, but should be"

    def search_items_found(self):
        search_input = self.browser.find_element(*ProductPageLocators.SEARCH_INPUT)
        search_btn = self.browser.find_element(*ProductPageLocators.SEARCH_BTN)
        search_input.send_keys(ProductPageLocators.SEARCH_SUCCESS_TEXT)
        search_btn.click()
        assert self.is_elements_present(*ProductPageLocators.PRODUCT_NAME), \
            "Searched list is empty, but should not be"
