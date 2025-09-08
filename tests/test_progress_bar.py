from pages.progress_bar_page import ProgressBarPage

def test_progress_bar(driver):
    page = ProgressBarPage(driver)
    page.open()
    val = page.stop_when_leq(25)
    assert val <= 25
    val100 = page.wait_until_100_and_reset()
    assert val100 >= 100
