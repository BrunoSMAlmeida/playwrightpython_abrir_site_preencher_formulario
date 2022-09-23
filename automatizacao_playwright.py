from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://www.hashtagtreinamentos.com/curso-python/")
    pagina.fill('xpath=//*[@id="_form_1919_"]/div[1]/div[1]/div/input', 'Bruno')
    pagina.fill('xpath=//*[@id="_form_1919_"]/div[1]/div[2]/div/input', 'bruno4893@hotmail.com')
    pagina.click('xpath=//*[@id="_form_1919_submit"]')
    time.sleep(5)