from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        """
        Clica em um elemento. Se o Selenium falhar por causa de anúncio ou overlay,
        força o clique via JavaScript.
        """
        element = self.wait.until(EC.presence_of_element_located((by, locator)))
        try:
            self.wait.until(EC.element_to_be_clickable((by, locator))).click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
        return element
