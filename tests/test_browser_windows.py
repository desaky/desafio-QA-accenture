from pages.browser_windows_page import BrowserWindowsPage

def test_new_window(driver):
    page = BrowserWindowsPage(driver)
    page.open()
    main_handle = driver.current_window_handle
    page.click_new_window()
    text, main = page.switch_to_new_window_and_get_text()
    assert "This is a sample page" in text
    # fechar a nova janela e voltar
    driver.close()
    driver.switch_to.window(main_handle)
