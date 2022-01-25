import unittest
import csv
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_user(self):
        driver = self.driver
        driver.get('https://mydocfam.com')
        driver.implicitly_wait(10) 
        
        lista = []
        with open('registro.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
            
        x=0
        for linea in lista:            
            if(x==0):
                x=x+1        
            else:
                #Variables
                correo_operador = linea [9]
                contrasena = linea [10]
                correo = linea [0]
                contrasena_paciente = linea [1]
                confirmacion_contrasena = linea [2]
                nombre = linea [3]
                apellido_p = linea[4]
                apellido_m = linea [5]
                nacimiento = linea [6]
                sexo = linea[7]
                telefono = linea [8]
            
               # Share items
                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[1]/div[2]/a[1]').click()

            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')

                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo_operador)
                password.send_keys(contrasena)

                input = driver.find_element_by_css_selector('body > ngb-modal-window > div > div > div.modal-body > div > form > div > div > div > div:nth-child(1) > button')
                input.click()

                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
                
                #share profile
                submit_botton = driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[2]').click()

                driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div[1]/div[1]/button').click()

                email = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/input[1]')
                email.send_keys(correo)

                password = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/input[2]')
                password.send_keys(contrasena_paciente)

                confirm_password = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/input[3]')
                confirm_password.send_keys(confirmacion_contrasena)

                name=driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/input[4]')
                name.send_keys(nombre)

                first_name = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/input[5]')
                first_name.send_keys(apellido_p)  

                last_name = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div/input[6]')
                last_name.send_keys(apellido_m)

                date = driver.find_element_by_id('date')
                date.send_keys(nacimiento)

                select_sex = Select(driver.find_element_by_id('sexo'))
                select_sex.select_by_visible_text(sexo)

                number=driver.find_element_by_name('telefono')
                number.send_keys(telefono)

                self.assertTrue(email.is_enabled()
                and password.is_enabled()
                and confirm_password.is_enabled()
                and confirm_password.is_enabled()
                and name.is_enabled()
                and first_name.is_enabled()
                and last_name.is_enabled())

                         
                create_account = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/input')
                self.assertTrue(create_account.is_displayed())
                create_account.click()
                time.sleep(3)
    
                close_modal = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button')
                close_modal.click()

                # Get out System
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()       

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'registro_paciente'))