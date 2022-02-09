from selenium.webdriver.common.by import By


class ProductPageLocators:
    URL = "https://buy-in-10-seconds.company.site/search"
    PRODUCT_NAME = (By.CLASS_NAME, "grid-product__title-inner")
    LBL_IN_STOCK = (By.XPATH, "//div[contains(text(), 'Распродано')]")
    LBL_ON_SALE = (By.XPATH, "//div[contains(text(), 'Распродажа')]")
    CHECKBOX_IN_STOCK = (By.ID, "checkbox-in_stock")
    CHECKBOX_ON_SALE = (By.ID, "checkbox-on_sale")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[type='search'].form-control__text")
    SEARCH_BTN = (By.CLASS_NAME, "form-control__ico-btn")
    SEARCH_NOT_SUCCESS_TEXT = "asdf"
    SEARCH_SUCCESS_TEXT = "2"
    SEARCH_EMPTY_NOTICE = (By.CLASS_NAME, "search__notice")
