from re import S
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
import time
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class UploadStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_upload_studies(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.maximize_window()
        driver.implicitly_wait(1)
      
        lista = []
        with open('subir_estudio.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
           
        # x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1
            else:
                correo = linea [0]
                contrasena = linea [1]
                nombre = linea [2]
                estudio = linea [3]
                fecha = linea [4]
              
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
                time.sleep(5)

                close_modal = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button')
                close_modal.click()
                
                #share profile
                submit_botton = driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[2]').click()
                time.sleep(1)

                #share patient
                share_patient = driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div[2]/form/input')
                share_patient.clear()
                share_patient.send_keys(nombre)
                time.sleep(2)

                driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div[2]/button').click()
                time.sleep(5)
                
                # Click table
                driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]').click()
                time.sleep(1)
               
                # Click upload studie
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[4]').click()
                time.sleep(3)

                # # Study name patient
                study_name_patient = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[1]')
                study_name_patient.clear()
                study_name_patient.send_keys(estudio)
                
                # Date of realization
                date_realization_studie = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[2]')
                date_realization_studie.clear() 
                date_realization_studie.send_keys(fecha) 

                # Select file 
                upload_studies_file = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[4]')
                upload_studies_file.send_keys('C:\\Users\Ángel Cid\\Desktop\\pruebas Docfam\\Operador\\RecetaMedica.pdf')
                

                # Select the DICOM file
                upload_studies_dicom = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[5]')
                upload_studies_dicom.send_keys('C:\\Users\Ángel Cid\\Desktop\\pruebas Docfam\\Operador\\rayosx.jpg')
                time.sleep(2)

                # Button upload
                button_upload = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]')
                self.assertTrue(button_upload.is_displayed())
                button_upload.click()
                time.sleep(8)

                # Close table updload studie
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[1]/button').click()

                # Close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
                
                #  Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Subir_Estudios_Paciente'))