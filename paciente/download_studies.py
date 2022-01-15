import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv
import time

#Cases of test
class DownloadStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        
    #unit tests  
    def test_download_studies(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.maximize_window()
        driver.window_handles
        driver.implicitly_wait(1)
      
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

                # Button Medical records
                driver.find_element_by_xpath('/html/body/app-root/div/app-paciente-expediente/div/ul/li[3]').click()
                driver.implicitly_wait(2)

                # Button table
                driver.find_element_by_xpath('//*[@id="listaEstudios"]/tbody/tr[1]').click()

                # table study
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/div/button[1]').click()
                time.sleep(2)
                # driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[3]/div/button[2]').click()

                #  Change the controller to the original window or tab    
                for h in driver.window_handles[1:]:
                    driver.switch_to_window(h) 
                    driver.close() 
                    driver.switch_to_window(driver.window_handles[0])
               
                # Button close tables
                close = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button')
                close.click()
                time.sleep(3)

                #Get out
                driver.find_element_by_xpath('/html/body/app-root/div/app-paciente-expediente/app-navbar/div/div[1]/div[2]/nav/ul/li[6]').click()              
                time.sleep(2)
         
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Descargar_estudios'))                  