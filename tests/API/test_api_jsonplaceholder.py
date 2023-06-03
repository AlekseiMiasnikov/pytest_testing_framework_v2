from core.utils.allure_wrapper import allure_wrapper
from core.utils.helpers import asserts
from data.jsonplaceholder import GET_RESPONSE_JSONPLACEHOLDER


class TestApiJsonPlaceHolder:
    @allure_wrapper(
        allure_title="api jsonplaceholder get",
        allure_suite="api suite",
        allure_parent_suite="api parent suite",
    )
    def test_api_jsonplaceholder_get(self, api_jsonplaceholder):
        asserts(
            actual_data=api_jsonplaceholder.jsonplaceholder_get(),
            asserts_data=GET_RESPONSE_JSONPLACEHOLDER
        )
