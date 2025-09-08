from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class BrowserWindowsPage(BasePage):
    URL = "https://demoqa.com/browser-windows"

    def open(self):
        super().open(self.URL)

    def click_new_window(self):
        self.click(By.ID, "windowButton")

    def switch_to_new_window_and_get_text(self):
        main = self.driver.current_window_handle
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != main:
                self.driver.switch_to.window(handle)
                break
        body = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        return body.text, main
