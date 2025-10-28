import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, wait, url):
        self.driver = driver
        self.wait = wait
        self.url = url

    @allure.step('Открываем страницу и ожидаем ее загрузки')
    def open(self):
        self.driver.get(self.url)
        self.wait.until(EC.url_contains(self.url))

    @allure.step('Находим элемент и кликаем')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Вводим текст в поле')
    def set_value(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Проверяем видимость элемента')
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Закрываем текущую вкладку')
    def close_current_tab(self):
        self.driver.close()

    @allure.step('Переключаемся на вкладку по индексу')
    def switch_to_tab(self, tab_index):
        tabs = self.driver.window_handles
        if tab_index < len(tabs):
            self.driver.switch_to.window(tabs[tab_index])

    @allure.step('Получаем количество открытых вкладок')
    def get_tabs_count(self):
        return len(self.driver.window_handles)

    @allure.step('Обновляем страницу')
    def refresh_page(self):
        self.driver.refresh()

    @allure.step('Возвращаемся на предыдущую страницу')
    def go_back(self):
        self.driver.back()

    @allure.step('Переходим на следующую страницу')
    def go_forward(self):
        self.driver.forward()