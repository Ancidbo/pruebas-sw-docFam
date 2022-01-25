import unittest
import csv, operator
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class ServiceHours(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_service_hours(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('data.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1        
            else:
                correo = linea [0]
                contrasena = linea [1]
                lunes_Viernes_inicio = linea [32]
                lunes_viernes_fin = linea [33]
                sabado_inicio = linea [34]
                sabado_fin = linea [35]
                domingo_inicio = linea [36]
                domingo_fin = linea [37]

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
                # Button configuration
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[6]').click()

                # Button Service hours
                driver.find_element_by_xpath('//*[@id="footer"]/div/div/ul/button[3]').click()

            # Service hours
                # Monday -  friday 
                monday_friday_start = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[1]/input[1]')
                monday_friday_start.clear()
                monday_friday_start.send_keys(lunes_Viernes_inicio)

                monday_friday_end = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[1]/input[2]')
                monday_friday_end.clear()
                monday_friday_end.send_keys(lunes_viernes_fin)

                # Button Modify
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[1]/button').click()

                # Saturday
                saturday_start = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[2]/input[1]')
                saturday_start.clear()
                saturday_start.send_keys(sabado_inicio)

                saturday_end = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[2]/input[2]')
                saturday_end.clear()
                saturday_end.send_keys(sabado_fin)
                
                # Button Modify
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[2]/button').click()


                # Sunday
                sunday_start = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[3]/input[1]')
                sunday_start.clear()                
                sunday_start.send_keys(domingo_inicio)


                sunday_end = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[3]/input[2]')
                sunday_end.clear()
                sunday_end.send_keys(domingo_fin)
                
                # Button Modify
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form[3]/button').click()

                # Close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()

                #  Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()
                
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Horario de servicio'))