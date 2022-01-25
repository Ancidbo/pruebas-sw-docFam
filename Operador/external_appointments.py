import unittest
import csv, operator
import smtplib
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

#unit tests
#Cases of test
class ExternalAppointments(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_external_appointments(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('subir_estudio.csv') as data:
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

                input = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/form/div/div/div/div[1]/button')
                input.click()
                time.sleep(5)

                close_modal = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button')
                close_modal.click()
                time.sleep(1)

            #  Botton open appointment 
                driver.find_element_by_xpath('/html/body/app-root/div/app-citas/div[1]/div[1]/div[4]/button[3]').click()
                time.sleep(2)

                # select state
                select_state = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/select'))
                select_state.select_by_visible_text('Puebla')
                time.sleep(4)
                
                # Button External appointments
                driver.find_element_by_xpath('//*[@id="container-princ"]/app-citas/div[1]/div[1]/div[4]/button[4]').click()
                time.sleep(5)

                # Table External appointments
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/span').click() 

                # Close
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[2]/button').click()

                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button').click()
                
                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name = 'Citas_Externas'))              