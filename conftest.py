import pytest
from datetime import datetime
from utils import setup_driver

@pytest.fixture(scope="function")
def driver():
    d = setup_driver()
    yield d
    d.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            driver.save_screenshot(f"report_fallo_{item.name}_{timestamp}.png")