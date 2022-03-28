import fordev as fd
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox

#### SETUP #####
opt = Options()
opt.add_argument("--headless")
browser = Firefox(options=opt)
browser.get("https://www.situacao-cadastral.com/")

path = os.getcwd()

print("Insira o cpf a ser procurado: ")
cpf = input()

if fd.validators.is_valid_cpf(cpf):
    campo_consulta = browser.find_element(By.ID,"doc")
    campo_consulta.send_keys(cpf)
    browser.find_element(By.ID,"consultar").click()
    try:
        result = browser.find_element(By.ID,"resultado")
        # Caso queira uma screenshot do resultado da página descomentar
        #result.screenshot(path + '/result.png')
        print('\n' + result.text)
    except Exception as erro:
        print("CPF ainda não cadastrado ou erro na consulta")
    finally:
        browser.quit()


else:
    print("CPF INVÁLIDO")
