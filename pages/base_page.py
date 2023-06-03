from core.utils.allure_wrapper import step
from selene import have, command, Browser


class BasePage:
    def __init__(self, browser: Browser):
        self.driver = browser
        self.el = self.driver.element

    # ... CHECK

    @step('Проверка наличия текста: {text}')
    def check_text(self, text, element='//body'):
        if type(text) != list:
            text = [text]
        for item in text:
            assert self.el(element).should(have.text(item))

    @step('Проверка отсутствия текста: {text}')
    def check_text_not_exist(self, text, element='//body'):
        if type(text) != list:
            text = [text]
        for item in text:
            self.el(element).should(have.no.text(item))

    # ... SPAN

    @step('Нажатие на: {text}')
    def click_span_text_idx(self, text, idx=1):
        self.el(f'//span[text() = "{text}"][{idx}]').click()

    @step('Нажатие на: {text}')
    def click_span_contains_text_idx(self, text, idx=1, use_js_click=False):
        if use_js_click:
            self.el(f'//span[contains(text(), "{text}")][{idx}]').perform(command=command.js.click)
        else:
            self.el('').click()

    # ... DIV

    @step('Нажатие на: {text}')
    def click_div_text_idx(self, text, idx=1):
        self.el(f'//div[text() = "{text}"][{idx}]').click()

    # ... INPUT

    @step('Нажатие на: {text}')
    def click_input_text_idx(self, text, idx=1):
        if type(text) != list:
            text = [text]
        for item in text:
            self.el(f'//input[text() = "{item}"][{idx}]').click()

    # ... BUTTON

    @step('Нажатие на: {text}')
    def click_button_text_idx(self, text, idx=1):
        self.el(f'//button[text() = "{text}"][{idx}]').click()

    # ... A

    @step('Нажатие на: {text}')
    def click_a_text_idx(self, text, idx=1, use_js_click=False):
        self.el(f'//a[text() = "{text}"][{idx}]').click()
