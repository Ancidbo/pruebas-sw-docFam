import unittest
import csv, operator
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class NewQuery(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_new_query(self):
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
                sexo_h_c = linea [47]
                peso_h_c = linea [48]
                talla_h_c = linea [49]
                fre_cardiaca_h_c = linea [50]
                temperatura_h_c = linea [51]
                sistole_h_c = linea [52]
                diastole_h_c = linea [53]
                especialidad_cita = linea [81]
                clinicos_cita = linea[82]
                impresion_diag_cita  = linea[83]
                recomendaciones_cita =linea [84]
                subjectivo_cita = linea [85]
                objectivo_cita = linea [86]
                analisis_cita = linea [87] 
                plan_cita = linea [88]
                titulo_cita = linea [89]
                nota_cita = linea [90]            
            
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

                # Button patient
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[2]').click()
                time.sleep(7)

                #  search patient
                search_patient = driver.find_element_by_xpath('/html/body/app-root/div/app-medico-paciente/div/div[2]/div[2]/div/div/div[2]/label/input')
                search_patient.clear()
                search_patient.send_keys(correo_paciente)

                # click table
                driver.find_element_by_xpath('/html/body/app-root/div/app-medico-paciente/div/div[2]/div[2]/div/div/table/tbody/tr').click()

                # Button new query
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[1]/div[3]/button').click()
                
                # Select specialty
                select_specialty = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/select')
                select_specialty.send_keys(especialidad_cita)

                # Button new query
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[2]/button[2]').click()

            # New Query

                # Clinicians
                clinicians = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[2]/textarea')
                clinicians.clear()
                clinicians.send_keys(clinicos_cita)

                # Diagnostic impression
                diagnostic_impression = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[3]/textarea')
                diagnostic_impression.clear()
                diagnostic_impression.send_keys(impresion_diag_cita)

                # Management recommendations
                management_recommendations = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[4]/textarea')
                management_recommendations.clear()
                management_recommendations.send_keys(recomendaciones_cita)

                 # Sex
                selec_sex = driver.find_element_by_xpath('//*[@id="sexo"]')
                selec_sex.send_keys(sexo_h_c)

                # weight
                weight = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[6]/div[2]/input')
                weight.clear()
                weight.send_keys(peso_h_c)

                # Size
                size = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[7]/div[2]/input')
                size.clear()
                size.send_keys(talla_h_c)
                # time.sleep(2)

                # Heart rate
                heart_rate = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[9]/div[2]/input')
                heart_rate.clear()
                heart_rate.send_keys(fre_cardiaca_h_c)

                # Breathing frequency
                breathing_frequency = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[2]/div[10]/div[2]/input')
                breathing_frequency.clear()
                breathing_frequency.send_keys (fre_cardiaca_h_c)

                # Temperature
                temperature = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[3]/div[2]/input')
                temperature.clear()
                temperature.send_keys(temperatura_h_c)

                # Sístole
                sistole = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[4]/div[3]/input')
                sistole.clear()
                sistole.send_keys(sistole_h_c)

                # Diástole
                diastole = driver.find_element_by_xpath('//*[@id="t-not-gral"]/div/div[5]/div[2]/input')
                diastole.clear()
                diastole.send_keys(diastole_h_c)
                time.sleep(2)

                self.assertTrue(clinicians.is_enabled()
                and diagnostic_impression.is_enabled()
                and management_recommendations.is_enabled()
                and weight.is_enabled()
                and heart_rate.is_enabled()
                and breathing_frequency.is_enabled()
                and temperature.is_enabled()
                and sistole.is_enabled()
                and diastole.is_enabled())

            # SOAP
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/ul/li[2]').click()

                # Subjective
                subjective = driver.find_element_by_xpath('//*[@id="t-not-soap"]/div/div/div[1]/textarea')
                subjective.clear()
                subjective.send_keys(subjectivo_cita)


                # Objective
                objective = driver.find_element_by_xpath('//*[@id="t-not-soap"]/div/div/div[2]/textarea')
                objective.clear()
                objective.send_keys(objectivo_cita)


                # Analysis
                analysis = driver.find_element_by_xpath('//*[@id="t-not-soap"]/div/div/div[3]/textarea')
                analysis.clear()
                analysis.send_keys(analisis_cita)


                # Plan
                plan = driver.find_element_by_xpath('//*[@id="t-not-soap"]/div/div/div[4]/textarea')
                plan.clear()
                plan.send_keys(plan_cita)

                self.assertTrue(subjective.is_enabled()
                and objective.is_enabled()
                and analysis.is_enabled()
                and plan.is_enabled())


            # Note    
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/ul/li[3]/a').click()

                # Title
                title = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[1]/input')
                title.clear()
                title.send_keys(titulo_cita)

                # Note
                note = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[1]/textarea')
                note.clear()
                note.send_keys()
                
                # Title1
                title1 = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[2]/input')
                title1.clear()
                title1.send_keys(titulo_cita)
                
                # Note1
                note1 = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[2]/textarea')
                note1.clear()
                note1.send_keys(nota_cita)

                # Title2
                title2 = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[3]/input')
                title2.clear()
                title2.send_keys(titulo_cita)

                # Note2
                note2 = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[3]/textarea')
                note2.clear()
                note2.send_keys(nota_cita)

                # Title3
                title3 = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[4]/input')
                title3.clear()
                title3.send_keys(titulo_cita)

                # Note3
                note3 = driver.find_element_by_xpath('//*[@id="t-not-notas"]/div/div[4]/textarea')
                note3.clear()
                note3.send_keys(nota_cita)

                self.assertTrue(title.is_enabled()
                and note.is_enabled()
                and title1.is_enabled()
                and note1.is_enabled()
                and title2.is_enabled()
                and note2.is_enabled()
                and title3.is_enabled()
                and note3.is_enabled())

                # Update
                button_update = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/button[2]')
                self.assertTrue(button_update.is_enabled)
                button_update.click()

                # Close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()

              # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Nueva consulta')) 