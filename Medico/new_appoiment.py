import unittest
import csv, operator
import smtplib
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class NewAppoiment(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_appoiment(self):
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
                # cie10 = linea [2]
                estudio = linea [3]
                tipo_cita = linea [4]
                costo = linea [5]
                fecha_estudio = linea [6]
                hora_i = linea [7]
                hora_f = linea [8]
                telefono = linea [9]

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


                # Button  new appoiment
                driver.find_element_by_xpath('//*[@id="container-princ"]/app-medico/div[1]/div[1]/div[1]/button[1]').click()
            
            # New appoiment
                # Study to be carried out
                new_appoiment = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[1]')
                new_appoiment.clear()
                new_appoiment.send_keys(estudio)

                # Select appoiment type
                select_appoiment = Select(driver.find_element_by_id('tipo')) 
                select_appoiment.select_by_visible_text(tipo_cita)

                # Cost
                cost = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[2]')
                cost.clear()
                cost.send_keys(costo)

                # Date
                date = driver.find_element_by_id('date')
                date.send_keys(fecha_estudio)
                
                # Start Time
                start_time = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[4]')
                start_time.send_keys(hora_i)

                # final time
                final_time = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[5]')
                final_time.send_keys(hora_f)

                # Phone
                phone = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/div/input[1]')
                phone.send_keys(telefono)

                self.assertTrue(new_appoiment.is_enabled()
                and cost.is_enabled()
                and date.is_enabled()
                and start_time.is_enabled()
                and final_time.is_enabled()
                and phone.is_enabled())

                # Button appoiment
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/button[2]').click()

                # Button return
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()

                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()






if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Nueva cita')) 