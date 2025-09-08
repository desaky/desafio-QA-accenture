from pages.form_page import FormPage

def test_practice_form(driver):
    page = FormPage(driver)
    page.open()
    page.fill_form()
    page.submit()
    txt = page.get_popup_text()
    assert "Thanks for submitting the form" in txt
    page.close_popup()
