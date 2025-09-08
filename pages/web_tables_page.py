from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class WebTablesPage(BasePage):
    URL = "https://demoqa.com/webtables"

    def open(self):
        super().open(self.URL)

    def click_add(self):
        self.click(By.ID, "addNewRecordButton")

    def add_record(self, first, last, email, age, salary, dept):
        self.find(By.ID, "firstName").send_keys(first)
        self.find(By.ID, "lastName").send_keys(last)
        self.find(By.ID, "userEmail").send_keys(email)
        self.find(By.ID, "age").send_keys(str(age))
        self.find(By.ID, "salary").send_keys(str(salary))
        self.find(By.ID, "department").send_keys(dept)
        self.click(By.ID, "submit")

    def search(self, text):
        el = self.find(By.ID, "searchBox")
        el.clear()
        el.send_keys(text)

    def delete_first_result(self):
        self.click(By.CSS_SELECTOR, "span[title='Delete']")

    def edit_first_result(self, new_first):
        self.click(By.CSS_SELECTOR, "span[title='Edit']")
        first_input = self.find(By.ID, "firstName")
        first_input.clear()
        first_input.send_keys(new_first)
        self.click(By.ID, "submit")
