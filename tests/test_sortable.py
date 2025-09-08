from pages.sortable_page import SortablePage
import time

def test_sortable(driver):
    page = SortablePage(driver)
    page.open()
    items = page.get_list_items()
    texts = [it.text.strip() for it in items]

    # vamos ordenar alfabeticamente os textos como exemplo de "ordem crescente"
    target = sorted(texts, key=lambda s: s.lower())

    # rearranjar: para cada posição, traga o item que deve estar ali
    for idx, name in enumerate(target):
        current_items = page.get_list_items()
        # localizar o elemento atualmente com esse nome
        source = next((el for el in current_items if el.text.strip() == name), None)
        if source is None:
            continue
        dest = current_items[idx]
        page.drag_to_position(source, dest)
        time.sleep(0.25)

    final = [el.text.strip().lower() for el in page.get_list_items()]
    assert final == [t.lower() for t in target]
