import sys
import time 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def main(argv):
    #### SETUP #####
    soft_names = [SoftwareName.FIREFOX.value]
    op_sys = [OperatingSystem.LINUX.value,OperatingSystem.WINDOWS.value]
    user_agent_rotator = UserAgent(software_names=soft_names,operating_systems=op_sys,limit=1000)
    usuario = user_agent_rotator.get_random_user_agent()
    opt = Options()
    opt.add_argument("start-maximized")
    opt.add_argument("--headless")
    opt.add_argument(f'user-agent={usuario}')
    browser = Firefox(options=opt)
    try:
        cpf = argv[0]
    except:
        print("Usage:\n\t./consulta-cpf {cpf}\n\tpython3 seleniumapp.py {cpf}")
        return
    
    #print("Insira o cpf a ser procurado: ")
    #cpf = input()

    browser.get("https://www.situacao-cadastral.com/")
    time.sleep(1) #evitando cloudflare flag
    campo_consulta = browser.find_element(By.ID,"doc")
    campo_consulta.send_keys(cpf)
    time.sleep(0.25)
    browser.find_element(By.ID,"consultar").click()
    try:
        result = WebDriverWait(browser,1).until(EC.presence_of_element_located((By.ID,"resultado")))
        # Caso queira uma screenshot do resultado da página descomentar
        #result.screenshot(path + '/result.png')
        print('\n' + result.text)
    except TimeoutException:
        print("deu timeout cloudflare me bloqueou")
    except Exception as erro:
        print(erro)
    finally:
        browser.quit()

if __name__ == '__main__':
    main(sys.argv[1:])

