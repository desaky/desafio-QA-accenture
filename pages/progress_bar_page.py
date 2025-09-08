from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProgressBarPage(BasePage):
    URL = "https://demoqa.com/progress-bar"

    def open(self):
        self.driver.get(self.URL)

    def click_start_stop(self):
        # botão muda de label (Start / Stop / Reset), mas o id é fixo
        btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "startStopButton"))
        )
        btn.click()

    def get_value(self):
        bar = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='progressbar']"))
        )
        return int(bar.get_attribute("aria-valuenow"))

    def stop_when_leq(self, threshold=25):
        self.click_start_stop()  # Start
        val = 0
        while True:
            val = self.get_value()
            if val >= threshold:
                self.click_start_stop()  # Stop
                break
        return val

    def wait_until_100_and_reset(self):
        self.click_start_stop()  # Start novamente
        self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.CSS_SELECTOR, "div[role='progressbar']"), "aria-valuenow", "100"
            )
        )
        # agora botão vira "Reset", mas ainda tem o mesmo id
        self.click_start_stop()
        # garantir que voltou a 0
        self.wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.CSS_SELECTOR, "div[role='progressbar']"), "aria-valuenow", "0"
            )
        )
        return 0
