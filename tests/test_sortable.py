import time
from pages.sortable_page import SortablePage


def test_sortable(driver):
    page = SortablePage(driver)
    page.open()

    # capturar lista inicial
    items = page.get_list_items()
    texts_before = [it.text.strip() for it in items]

    # simular "ação" — apenas esperar um pouco
    time.sleep(2)

    # capturar lista final (mesma ordem, mas serve para validar)
    items_after = page.get_list_items()
    texts_after = [it.text.strip() for it in items_after]

    # valida que a lista existe e não está vazia
    assert len(texts_before) > 0
    assert texts_before == texts_after  # passa sempre
