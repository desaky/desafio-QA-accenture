import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProgressBarPage(BasePage):
    URL = "https://demoqa.com/progress-bar"

    def open(self):
        super().open(self.URL)

    def click_start_stop(self):
        btn = self.find(By.ID, "startStopButton")
        # garante que o botão esteja visível e clica via JS
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    def get_progress_value(self):
        el = self.find(By.CLASS_NAME, "progress-bar")
        style = el.get_attribute("style") or ""
        if "width" in style:
            try:
                return int(style.split("width:")[1].split("%")[0].strip())
            except:
                pass
        text = el.text.strip().replace("%", "")
        try:
            return int(text)
        except:
            return 0

    def stop_when_leq(self, threshold=25, timeout=10):
        self.click_start_stop()  # start
        start = time.time()
        last_val = 0
        while time.time() - start < timeout:
            val = self.get_progress_value()
            if val > 0 and val <= threshold:
                self.click_start_stop()  # stop
                return val
            last_val = val
            time.sleep(0.15)
        self.click_start_stop()
        return last_val

    def wait_until_100_and_reset(self, timeout=30):
        self.click_start_stop()  # start
        start = time.time()
        while time.time() - start < timeout:
            val = self.get_progress_value()
            if val >= 100:
                self.click_start_stop()  # reset
                return val
            time.sleep(0.2)
        return self.get_progress_value()
