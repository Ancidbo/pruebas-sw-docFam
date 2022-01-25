import unittest
import csv, operator
import smtplib
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class NewAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_appointment(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('agendar.csv') as data:
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
                contrasenia = linea [1]
                sucursal = linea [2]
                sala = linea [3]
                estado = linea [4]
                prueba = linea [5]
                fecha_cita = linea [6]
                hora_i = linea [7]
                paciente = linea [8] 

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

                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
                    
            #schedule appointment
                # Select branch
                select_branch = Select(driver.find_element_by_id('inlineFormCustomSelect')) 
                select_branch.select_by_visible_text(sucursal)

                # Select hall
                select_hall = Select(driver.find_element_by_xpath('/html/body/app-root/div/app-citas/div[1]/div[1]/div[2]/select')) 
                select_hall.select_by_visible_text(sala)

                #New appointment
                new_quote = driver.find_element_by_xpath('//*[@id="container-princ"]/app-citas/div[1]/div[1]/div[4]/button[1]').click()


                
                # Create Appointment
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/div[1]/button').click()

                # select state
                select_state = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div/select'))
                select_state.select_by_visible_text(estado)

                test = driver.find_element_by_xpath('//*[@id="search-banner"]/div/div/div[1]/div/div/div/div[1]/div/input')
                test.clear()
                test.send_keys(prueba)
                
                self.assertTrue(test.is_enabled())
                # search
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/button').click()
               
                # Select studie
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div/div/div[2]/div/article/button[2]').click()

                # Date
                date = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[2]')
                date.send_keys(fecha_cita)

                # Start Time
                start_time = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[3]')
                start_time.send_keys(hora_i)

                # Final time
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/button').click()
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/button[2]').click()
                    
                # select patient
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/div[2]/button[1]').click()

                patient = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input')
                patient.send_keys(paciente)
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]').click()

                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div/table/tbody/tr/td[2]').click()
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]').click()
                
                # Schedule
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/button[2]').click()

                # Get out
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/button[1]').click()

                # Get out System
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()       

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Nueva_cita'))