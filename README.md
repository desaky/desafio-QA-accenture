# Desafio QA Accenture

Este projeto foi feito como parte do desafio técnico.  
A ideia foi criar testes automatizados para **API** e **Front-End**, usando **Python + Pytest + Selenium**.

------------------------------------------------------------------------------------------------------------

## Estrutura do projeto

- `tests/` → Onde ficam os testes automatizados.
- `pages/` → Page Objects usados para organizar os testes de UI.
- `conftest.py` → Configuração do Selenium WebDriver.
- `requirements.txt` → Dependências do projeto.

--------------------------------------------------------------------------------------------------------------

## Como rodar os testes

Crie e ative o ambiente virtual:


    python -m venv venv
    source venv/Scripts/activate   # Windows
    # ou
    source venv/bin/activate       # Linux/Mac

## Instale as dependências:
    ```bash
    pip install -r requirements.txt

## Agora você pode rodar os testes separadamente:
    ```bash
    pytest tests/test_api_flow.py -v

* API:
    ```bash
  pytest tests/test_api_flow.py -v

* Forms:
    ```bash
    pytest tests/test_forms.py -v --headed

* Browser windows:
    ```bash
    pytest tests/test_browser_windows.py -v --headed

* Web Tables: 
    ```bash
    pytest tests/test_web_tables.py -v --headed


* Sortable:
    ```bash
    pytest tests/test_sortable.py -v --headed

* Progress Bar:
    ```bash
 pytest tests/test_progress_bar.py -v --headed

##Observações importantes!

    * O site de testes DemoQA às vezes carrega muitos anúncios que atrapalham o Selenium (por exemplo, no teste da progress bar).

    * Por isso, alguns códigos foram adaptados para contornar esses problemas.