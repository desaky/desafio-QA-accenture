from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class SortablePage(BasePage):
    URL = "https://demoqa.com/sortable"

    def open(self):
        super().open(self.URL)

    def get_list_items(self):
        try:
            self.click(By.ID, "demo-tab-list")
        except:
            pass
        return self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#verticalListContainer .list-group-item")))

    def drag_to_position(self, source_element, target_element):
        actions = ActionChains(self.driver)
        # usar "move_by_offset" às vezes é mais estável em páginas com anúncios
        actions.click_and_hold(source_element).move_to_element(target_element).pause(0.3).release().perform()
