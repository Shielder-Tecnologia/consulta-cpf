import fordev as fd
import os
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

#### SETUP #####
soft_names = [SoftwareName.FIREFOX.value]
op_sys = [OperatingSystem.LINUX.value,OperatingSystem.WINDOWS.value]
user_agent_rotator = UserAgent(software_names=soft_names,operating_systems=op_sys,limit=100)
usuario = user_agent_rotator.get_random_user_agent()
opt = Options()
opt.add_argument("--headless")
opt.add_argument(f'user-agent={usuario}')
browser = Firefox(options=opt)

path = os.getcwd()

print("Insira o cpf a ser procurado: ")
cpf = input()

if fd.validators.is_valid_cpf(cpf):
    browser.get("https://www.situacao-cadastral.com/")
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
