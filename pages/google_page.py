from core.utils.allure_wrapper import step
from core.utils.helpers import get_env_option
from pages import BasePage


class GooglePage(BasePage):

    @step('Открытие страницы')
    def open(self, url='/'):
        self.driver.open(f"{get_env_option(option='GOOGLE_URL')}{url}")

    @step('Ввод в поиск: {value}')
    def fill_search_form(self, value):
        self.el('//*[@type="search"]').set_value(value)
