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
        driver.get('https://mydocfam.com/registro')
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
                correo = linea [0]
                contrasena = linea[1]
                nombre = linea [3]
                apellido_p = linea[4]
                apellido_m = linea [5]
                fecha= linea[6]  
                sexo = linea[7]
                telefono = linea [8]
                
               
                email = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[1]/input')
                email.clear()
                email.send_keys(correo)

                password = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[2]/input')
                password.clear()
                password.send_keys(contrasena)

                confirm_password = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[3]/input')
                confirm_password.clear()
                confirm_password.send_keys(contrasena)

                name=driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[4]/input')
                name.clear()
                name.send_keys(nombre)

                first_name = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[5]/input')
                first_name.clear()
                first_name.send_keys(apellido_p)  

                last_name = driver.find_element_by_xpath('/html/body/app-root/div/app-register/body/div/div/div/div[2]/div[6]/input')
                last_name.clear()
                last_name.send_keys(apellido_m)

                date = driver.find_element_by_id('date')
                date.clear()
                date.send_keys(fecha)

                select_sex = Select(driver.find_element_by_id('sexo'))
                select_sex.select_by_visible_text(sexo)

                number=driver.find_element_by_name('telefono')
                number.clear()
                number.send_keys(telefono)

                self.assertTrue(email.is_enabled()
                and password.is_enabled()
                and confirm_password.is_enabled()
                and confirm_password.is_enabled()
                and name.is_enabled()
                and first_name.is_enabled()
                and last_name.is_enabled())

                         
                create_account = driver.find_element_by_xpath('//*[@id="container-princ"]/app-register/body/div/div/div/div[2]/div[10]/button')
                self.assertTrue(create_account.is_displayed())
                create_account.click()
    
                accept_terms = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[2]')
                self.assertTrue(accept_terms.is_displayed())
                accept_terms.click()
                time.sleep(2)

                closed_win = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button')
                self.assertTrue(closed_win.is_displayed())
                closed_win.click()
                
                driver.refresh()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'registro_paciente'))