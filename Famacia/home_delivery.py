import unittest
import csv
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time 

#unit tests
#Cases of test
class HomeDelivery(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_home_delivery(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('farmacia.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
            if(x==0):
                x=x+1        
            else:
                correo = linea [0]
                contrasena = linea [1]
                estado = linea [2]
                ciudad = linea [3]
                estatus = linea [4]
                nota = linea [5]
                status = linea [7]

                           
            # Share items
                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[1]/div[2]/a[1]').click()

            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')

                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasena)

                input = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/form/div/div/div/div[1]/button')
                input.click()
                
                close_modal = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button')
                close_modal.click()

                # Select state and city
                state = Select(driver.find_element_by_xpath('//*[@id="inlineFormCustomSelect"]')) 
                state.select_by_visible_text(estado)
                
                city = Select(driver.find_element_by_xpath('/html/body/app-root/div/app-medicamentos/div/div/div/div[1]/div/div[3]/select')) 
                city.select_by_visible_text(ciudad)

                # search
                search = driver.find_element_by_xpath('/html/body/app-root/div/app-medicamentos/div/div/div/div[2]/div/div/div[2]/label/input')
                search.send_keys(estatus)

                driver.find_element_by_xpath('/html/body/app-root/div/app-medicamentos/div/div/div/div[2]/div/div/table/tbody/tr[1]').click()

                # medication list
                medication_list = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[1]/div[4]/button')
                medication_list.click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button').click()
                time.sleep(1)
                # patient contact
                patient_contact = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[1]/div[5]/button')
                patient_contact.click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button').click()

                # Edit
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/button[3]').click()
                note = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input')
                note.clear()
                note.send_keys(nota)
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]').click()
                time.sleep(1)
                
                # Modify Status
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/button[2]').click()
                modify_estatus = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/select'))
                modify_estatus.select_by_visible_text(status)
                time.sleep(1)

                # Select Messenger
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/button').click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/ngb-modal-window[3]/div/div/div[2]/div/div/table/tbody/tr').click()
                time.sleep(1)

                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]').click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/button').click()
                time.sleep(1)
                # get out system
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()
                
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Envio Medicamento'))