import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run with browser visible (not headless)")

@pytest.fixture(scope="session")
def driver(request):
    opts = webdriver.ChromeOptions()
    # rodar em headless por padrão; fale --headed para ver o browser
    if not request.config.getoption("--headed"):
        # new headless mode; se der problema, remova '--headless=new' e use '--headless'
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
