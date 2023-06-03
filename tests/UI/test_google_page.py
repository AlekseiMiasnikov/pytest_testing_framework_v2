from time import sleep

from pytest import mark

from core.utils.allure_wrapper import allure_wrapper


class TestGoogleSearchGroup1:
    @allure_wrapper(
        allure_title="Checking the Google search page",
        allure_suite="Checking the Google search page",
        allure_parent_suite="Checking the Google search page",
    )
    @mark.google
    def test_google_search(self, google_page):
        google_page.open()
        google_page.fill_search_form(value='TESTING ME, PLEASE')
        google_page.check_text(text='')


class TestGoogleSearchGroup2:
    @allure_wrapper(
        allure_title="Checking the Google search page",
        allure_suite="Checking the Google search page",
        allure_parent_suite="Checking the Google search page",
    )
    @mark.google
    def test_google_search_two(self, google_page):
        google_page.open()
        google_page.fill_search_form(value='TESTING ME, PLEASE')
        google_page.check_text(text='')
        sleep(5)

    @allure_wrapper(
        allure_title="Checking the Google search page",
        allure_suite="Checking the Google search page",
        allure_parent_suite="Checking the Google search page",
    )
    @mark.google
    def test_google_search_two(self, google_page):
        google_page.open()
        google_page.fill_search_form(value='TESTING ME, PLEASE')
        google_page.check_text(text='')
