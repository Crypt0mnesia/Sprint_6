import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage

from helper import generate_order_data
from urls import ORDER_PAGE_URL, MAIN_PAGE_URL, DZEN_URL, TRACK_PAGE_URL

class TestOrderFlow:
    @allure.title('Позитивный сценарий заказа с точкой входа: {entry_point}')
    @pytest.mark.parametrize('entry_point, order_data', [
        ('top', generate_order_data()),
        ('bottom', generate_order_data())
    ])
    def test_successful_order_complete_flow(self, driver, wait, entry_point, order_data):
        main_page = MainPage(driver, wait)
        order_page = OrderPage(driver,wait)
        order_data = generate_order_data()

        main_page.open()

        click_methods = {
            'top': main_page.click_top_order_button,
            'bottom': main_page.click_bottom_order_button
        }
        click_methods[entry_point]()

        order_page.fill_first_part(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['metro_station'],
            order_data['phone']
        )

        order_page.fill_second_part(
            order_data['date'],
            order_data['rental_period'],

        )

        order_page.confirm_order()

        order_number = order_page.get_order_number()
        assert order_number is not None

        order_page.go_to_order_status()
        assert TRACK_PAGE_URL in driver.current_url