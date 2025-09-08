import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from faker import Faker

fake = Faker()

class FormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    def open(self):
        super().open(self.URL)

    def fill_form(self):
        self.find(By.ID, "firstName").send_keys(fake.first_name())
        self.find(By.ID, "lastName").send_keys(fake.last_name())
        self.find(By.ID, "userEmail").send_keys(fake.email())
        self.click(By.CSS_SELECTOR, "label[for='gender-radio-1']")
        self.find(By.ID, "userNumber").send_keys("9876543210")

        # upload file
        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(base_dir, "resources", "upload.txt")
        self.find(By.ID, "uploadPicture").send_keys(file_path)

        self.find(By.ID, "currentAddress").send_keys(fake.address())

    def submit(self):
        self.click(By.ID, "submit")

    def get_popup_text(self):
        modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        return modal.text

    def close_popup(self):
        self.click(By.ID, "closeLargeModal")
