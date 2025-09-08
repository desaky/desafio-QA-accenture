from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class SortablePage(BasePage):
    URL = "https://demoqa.com/sortable"

    def open(self):
        self.driver.get(self.URL)

    def get_list_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")
            )
        )
