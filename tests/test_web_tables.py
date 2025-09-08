from pages.web_tables_page import WebTablesPage
from faker import Faker
import time

fake = Faker()

def test_web_tables_crud(driver):
    page = WebTablesPage(driver)
    page.open()
    page.click_add()
    first = fake.first_name()
    last = fake.last_name()
    email = fake.email()
    age = 30
    salary = 1000
    dept = "QA"
    page.add_record(first, last, email, age, salary, dept)

    # pesquisar pelo primeiro nome
    page.search(first)
    time.sleep(0.5)
    assert first in driver.page_source

    # editar
    page.edit_first_result(first + "_edited")
    page.search(first + "_edited")
    time.sleep(0.5)
    assert (first + "_edited") in driver.page_source

    # deletar
    page.delete_first_result()
    page.search(first + "_edited")
    time.sleep(0.5)
    # depois de deletar pode aparecer "No rows found"
    assert ("No rows found" in driver.page_source) or (first + "_edited" not in driver.page_source)
