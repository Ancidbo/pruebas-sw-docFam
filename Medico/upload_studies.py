import unittest
import csv, operator
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class UploadStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_upload_studies(self):
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
                correo_paciente = linea [13]
                nombre_estudio = linea [38]
                fecha_r_estudio = linea [39]

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


                # Button patients
                driver.find_element_by_xpath('/html/body/app-root/div/app-medico/app-nav-med/div/div[1]/div[2]/nav/ul/li[2]').click()
                time.sleep(4)

                # Search
                search_patient = driver.find_element_by_xpath('/html/body/app-root/div/app-medico-paciente/div/div[2]/div[2]/div/div/div[2]/label/input')
                search_patient.clear()
                search_patient.send_keys(correo_paciente)

                # Click table
                driver.find_element_by_xpath('/html/body/app-root/div/app-medico-paciente/div/div[2]/div[2]/div/div/table/tbody/tr').click()

                # Button studies
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ul/li[4]/a').click()
                time.sleep(1)

                # Button Upload studies
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/div[4]/div/button').click()
                time.sleep(1)

                # Study name patient
                study_name_patient = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[1]')
                study_name_patient.clear()
                study_name_patient.send_keys(nombre_estudio)
                
                # Date of realization
                date_realization_studie = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[2]')
                date_realization_studie.clear() 
                date_realization_studie.send_keys(fecha_r_estudio) 

                # Select file 
                upload_studies_file = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[4]')
                upload_studies_file.send_keys('C:\\Users\\Semin\\Desktop\\medico\\RecetaMedica.pdf')

                # Select the DICOM file
                upload_studies_dicom = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[5]')
                upload_studies_dicom.send_keys('C:\\Users\\Semin\\Desktop\\medico\\rayosx.jpg')

                # Button upload
                button_upload = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]')
                self.assertTrue(button_upload.is_displayed())
                button_upload.click()
                time.sleep(2)

                # Close table updload studie
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[1]/button').click()

                # Close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
                
                #  Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Subir Estudios')) 