from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    # добавление товара в корзину
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    #расчёт математического выражения
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def message_about_product_add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCES_MESSAGE_PRODUCT_IN_BASKET), "Сообщения об успешном добавлении товара в корзину нет"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == product_name_in_message, "Имя товара в сообщении отличается от имени добавляемого товара"

    def price_of_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUM_IN_BASKET), "Нет сообщения со стоимостью товара в корзине"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        assert product_price == product_price_in_message, "Стоимость товара в сообщении отличается от стоимости добавляемого товара"

