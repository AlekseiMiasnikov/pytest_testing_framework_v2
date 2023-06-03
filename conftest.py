from os import getenv
from typing import Any

import pytest
from selenium import webdriver
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from core.utils.helpers import get_settings, get_fixtures, get_current_folder
from selene.support.shared import config

from selene import Browser, Config
from selenium.webdriver import Firefox, Chrome

settings_config = {}
pytest_plugins = get_fixtures()


def pytest_sessionstart():
    global settings_config
    disable_warnings(InsecureRequestWarning)
    settings_config = get_settings(environment=getenv('environment'))


def pytest_addoption(parser):
    parser.addoption('--mode', action='store', default='local')
    parser.addoption('--browser', action='store', default='chrome')


def _create_driver_with_browser_name(*, browser_name='chrome', options):
    match browser_name:
        case "firefox":
            return Browser(
                Config(
                    driver=Firefox(
                        executable_path=GeckoDriverManager().install(),
                        options=options,
                    ),
                    base_url=settings_config['APP_URL'],
                    timeout=settings_config['TIMEOUT'],
                    driver_name=settings_config['BROWSER_NAME'],
                    window_width=settings_config['BROWSER_WINDOW_WIDTH'],
                    window_height=settings_config['BROWSER_WINDOW_HEIGHT']
                )
            )
        case 'ie':
            return webdriver.Ie(
                executable_path=IEDriverManager().install(),
                options=options
            )
        case _:
            return Browser(
                Config(
                    driver=Chrome(
                        executable_path=ChromeDriverManager().install(),
                        options=options,
                    ),
                    base_url=settings_config['APP_URL'],
                    timeout=settings_config['TIMEOUT'],
                    driver_name=settings_config['BROWSER_NAME'],
                    window_width=settings_config['BROWSER_WINDOW_WIDTH'],
                    window_height=settings_config['BROWSER_WINDOW_HEIGHT']
                )
            )


@pytest.fixture(scope='function')
def browser(pytestconfig: Any) -> Any:
    mode = pytestconfig.getoption('mode')
    browser_name = pytestconfig.getoption('browser')
    match browser_name:
        case 'firefox':
            options = webdriver.FirefoxOptions()
            options.set_preference('browser.download.dir', get_current_folder(folder='files'))
        case 'ie':
            options = webdriver.IeOptions()
        case _:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('prefs', {
                'profile.default_content_setting_values.notifications': 1,
                'download.default_directory': get_current_folder(folder='files'),
                'safebrowsing.enabled': True,
            })
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-infobars")
    options.add_argument("--privileged")
    options.add_argument("--disable-extensions")
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    settings_config['BROWSER_NAME'] = browser_name if browser_name != 'chrome' else settings_config['BROWSER_NAME']
    driver_browser = None
    match mode:
        case 'selenoid':
            capabilities = {
                'browserName': settings_config['BROWSER_NAME'],
                'browserVersion': settings_config['SELENOID']['BROWSER_VERSION'],
                'selenoid:options': {
                    'enableVNC': settings_config['SELENOID']['ENABLE_VNC'],
                    'enableVideo': settings_config['SELENOID']['ENABLE_VIDEO']
                }
            }
            config.driver = webdriver.Remote(
                command_executor=settings_config['SELENOID']['HUB'],
                desired_capabilities=capabilities,
                options=options
            )
        case 'headless':
            options.add_argument('--headless')
            driver_browser = _create_driver_with_browser_name(browser_name=browser_name, options=options)
            # config.execute_cdp_cmd('Page.setDownloadBehavior', {
            #     'behavior': 'allow',
            #     'downloadPath': get_current_folder(folder='files')
            # })
        case _:
            driver_browser = _create_driver_with_browser_name(browser_name=browser_name, options=options)
    config.save_screenshot_on_failure = False
    config.save_page_source_on_failure = False
    yield driver_browser
    driver_browser.quit()
