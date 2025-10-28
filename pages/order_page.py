import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from urls import ORDER_PAGE_URL

class OrderPage(BasePage):
    def __init__(self, driver, wait):
        super().__init__(driver, wait, ORDER_PAGE_URL)

    @allure.step('Заполнить первую часть формы заказа')
    def fill_first_part(self, name, surname, address, station_name, phone):
        self.set_value(OrderPageLocators.NAME_INPUT, name)
        self.set_value(OrderPageLocators.SURNAME_INPUT, surname)
        self.set_value(OrderPageLocators.ADDRESS_INPUT, address)
        self.set_value(OrderPageLocators.PHONE_INPUT, phone)

        self.click(OrderPageLocators.METRO_STATION_INPUT)
        self.wait.untill(EC.element_to_be_clickable(OrderPageLocators.METRO_DROPDOWN))
        station_locator = (
            OrderPageLocators.METRO_STATION_BY_NAME[0],
            OrderPageLocators.METRO_STATION_BY_NAME[1].format(station_name)
        )
        self.click(station_locator)

        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить вторую часть формы заказа')
    def fill_second_part(self, date, rental_period):
        self.set_value(OrderPageLocators.DATE_INPUT)

        self.click(OrderPageLocators.RENTAL_PERIOD_SELECT)
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_DROPDOWN))
        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION_BY_TEXT[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION_BY_TEXT[1].format(rental_period)
        )
        self.click(period_locator)

        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_text(OrderPageLocators.ORDER_NUMBER)

    @allure.step('Перейти к статусу заказа')
    def go_to_order_status(self):
        self.click(OrderPageLocators.STATUS_BUTTON)