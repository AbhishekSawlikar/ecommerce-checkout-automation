import pytest
import allure
from selenium import webdriver
from config.config import GRID_URL

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")
    parser.addoption("--grid", action="store_true", default=False, help="Run on remote Selenium Grid")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    use_grid = request.config.getoption("--grid")

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

    if use_grid:
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
    else:
        driver = webdriver.Chrome(options=options) if browser == "chrome" else webdriver.Firefox(options=options)

    driver.maximize_window()
    yield driver

    # Capture screenshot for Allure report on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="failure_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)