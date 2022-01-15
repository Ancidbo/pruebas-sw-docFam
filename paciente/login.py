import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
import csv
import time


#Cases of test
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_login(self):
        driver = self.driver
        driver.get('https://mydocfam.com/sitio/inicio')
        driver.maximize_window()
        driver.implicitly_wait(5)
      
        lista = []
        with open('agenda_estudio.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
            if(x==0):
                x=x+1
            else:
                correo = linea [0]
                contrasenia = linea [1]

                # Share items
                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[1]/div[2]/a[1]').click()

            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')

                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)

                input = driver.find_element_by_css_selector('body > ngb-modal-window > div > div > div.modal-body > div > form > div > div > div > div:nth-child(1) > button')
                input.click()
                driver.implicitly_wait(2)

                close = driver.find_element_by_css_selector('body > ngb-modal-window > div > div > div.modal-header > button')
                close.click()
                time.sleep(1)

                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[1]/div[2]/a').click()
                # time.sleep(1)
                #Get out
                driver.find_element_by_xpath('/html/body/app-root/div/app-paciente-expediente/app-navbar/div/div[1]/div[2]/nav/ul/li[6]').click()
     
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Login'))
