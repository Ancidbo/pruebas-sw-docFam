import unittest
import csv, operator
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class UpdateClinicalHistory(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_update_clinical_history(self):
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
                tipo_interrogatorio_h_c = linea[40]
                informador_h_c = linea [41]
                estado_de_naciemiento_h_c = linea[42]
                estado_salud_h_c = linea [43]
                tel_casa_h_c = linea [44]
                tel_ofi_h_c = linea [45]
                tel_cel_h_c = linea [46]
                sexo_h_c = linea [47]
                peso_h_c = linea [48]
                talla_h_c = linea [49]
                fre_cardiaca_h_c = linea [50]
                temperatura_h_c = linea [51]
                sistole_h_c = linea [52]
                diastole_h_c = linea [53]
                antecedentes_fami_h_c = linea [54]
                ante_fa_no_patológicos_h_c = linea [55]
                personales_patológicos_h_c = linea [56]
                proce_actual_h_c = linea [57]
                aux_diagnostico_h_c = linea [58]
                calle_h_c = linea [59]
                colonia_h_c = linea [60]
                numero_inter_h_c = linea [61]
                numero_exter_h_c = linea [62]
                cp_h_c = linea [63]
                municipio_h_c = linea [64]
                localidad_h_c = linea [65]
                estado_h_c = linea [66]
                estado_civil_h_c = linea [67]
                hijos_h_c = linea [68]
                mx_estudios_h_c = linea [69]
                ocupacion_h_c = linea [70]
                religion_h_c = linea [71]
                sis_digestivo_h_c = linea [72]
                sis_musculo_h_c = linea [73]
                sis_neurologico_h_c = linea [74]
                sis_reproductor_h_c = linea [75]
                sistema_respi_h_c = linea [76]
                sis_de_sentidos_h_c = linea [77]
                sis_tegumentario_h_c = linea [78]
                sis_urinario_h_c = linea [79]
                frecuencia_respi = linea [80]

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

                # Button Medical History
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/ul/li[2]/a').click()
                time.sleep(1)
                
                # Button update Medical History
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/div[2]/div/div[2]/button[2]').click()

            # General
                # Type of Interrogation
                select_type_interrogation = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/select[1]')
                select_type_interrogation.send_keys(tipo_interrogatorio_h_c)

                # Informer
                informer = driver.find_element_by_xpath('//*[@id="t-hist-gral"]/div/div[1]/input[1]')
                informer.clear()
                informer.send_keys(informador_h_c)

                # State of birth
                state_of_birth = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/select[2]')
                state_of_birth.send_keys(estado_de_naciemiento_h_c)

                # Health condition
                health_condition = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/input[2]')
                health_condition.clear()
                health_condition.send_keys(estado_salud_h_c)

                # Home phone
                home_phone = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/input[3]')
                home_phone.clear()
                home_phone.send_keys(tel_casa_h_c)

                # Office phone
                office_phone = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/input[4]')
                office_phone.clear()
                office_phone.send_keys(tel_ofi_h_c)

                # Cell phone
                cell_phone = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/input[5]')
                cell_phone.clear()
                cell_phone.send_keys(tel_cel_h_c)

                # Sex
                selec_sex = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/select[3]')
                selec_sex.send_keys(sexo_h_c)

                # weight
                weight = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/input')
                weight.clear()
                weight.send_keys(peso_h_c)

                # Size
                size = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/input')
                size.clear()
                size.send_keys(talla_h_c)
                # time.sleep(2)

                # Heart rate
                heart_rate = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/div[4]/div[2]/input')
                heart_rate.clear()
                heart_rate.send_keys(fre_cardiaca_h_c)

                # Breathing frequency
                breathing_frequency = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[1]/div[5]/div[2]/input')
                breathing_frequency.clear()
                breathing_frequency.send_keys(frecuencia_respi)

                # Temperature
                temperature = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/input')
                temperature.clear()
                temperature.send_keys(temperatura_h_c)

                # Sístole
                sistole = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[3]/div[3]/input')
                sistole.clear()
                sistole.send_keys(sistole_h_c )

                # Diástole
                diastole = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div[4]/div[2]/input')
                diastole.clear()
                diastole.send_keys(diastole_h_c)
                time.sleep(2)
                              
                self.assertTrue(informer.is_enabled() 
                and health_condition.is_enabled()
                and home_phone.is_enabled()
                and office_phone.is_enabled()
                and cell_phone.is_enabled()
                and weight.is_enabled()
                and size.is_enabled()
                and heart_rate.is_enabled()
                and breathing_frequency.is_enabled()
                and temperature.is_enabled()
                and sistole.is_enabled()
                and diastole.is_enabled())

            # Background
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/ul/li[2]').click()

                # Family background
                family_background = driver.find_element_by_xpath('//*[@id="t-hist-ant"]/div/div[1]/textarea')
                family_background.clear()
                family_background.send_keys(antecedentes_fami_h_c)

                # Non-pathological personal history
                non_pathological = driver.find_element_by_xpath('//*[@id="t-hist-ant"]/div/div[2]/textarea')
                non_pathological.clear()
                non_pathological.send_keys(ante_fa_no_patológicos_h_c)

                # Pathological personal history
                pathological = driver.find_element_by_xpath('//*[@id="t-hist-ant"]/div/div[3]/textarea') 
                pathological.clear()
                pathological.send_keys(personales_patológicos_h_c) 

                # Current procedure
                current_procedure = driver.find_element_by_xpath('//*[@id="t-hist-ant"]/div/div[4]/textarea')
                current_procedure.clear()
                current_procedure.send_keys(proce_actual_h_c )

                # Diagnostic aids
                diagnostic_aids = driver.find_element_by_xpath('//*[@id="t-hist-ant"]/div/div[5]/textarea')
                diagnostic_aids.clear()
                diagnostic_aids.send_keys(aux_diagnostico_h_c)

                self.assertTrue(family_background.is_enabled()
                and non_pathological.is_enabled()
                and pathological.is_enabled()
                and current_procedure.is_enabled()
                and diagnostic_aids.is_enabled()) 

            # Address
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/ul/li[3]/a').click()

                # Street
                street = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[1]')
                street.clear()
                street.send_keys(calle_h_c)

                # Suburb
                suburb = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[2]')
                suburb.clear()
                suburb.send_keys(colonia_h_c)

                # Interior number
                interior_number = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[3]')
                interior_number.clear()
                interior_number.send_keys(numero_inter_h_c)

                # Outdoor Number
                outdoor_number = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[4]')
                outdoor_number.clear()
                outdoor_number.send_keys(numero_exter_h_c)

                # CP
                cp = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[5]')
                cp.clear()
                cp.send_keys(cp_h_c)

                # Municipality
                municipality = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[6]')
                municipality.clear()
                municipality.send_keys(municipio_h_c)

                # Location
                location = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/input[7]')
                location.clear()
                location.send_keys(localidad_h_c)

                # State
                select_state = driver.find_element_by_xpath('//*[@id="t-hist-dir"]/div/div/select')
                select_state.send_keys(estado_h_c)

                self.assertTrue(street.is_enabled()
                and suburb.is_enabled()
                and interior_number.is_enabled()
                and outdoor_number.is_enabled()
                and cp.is_enabled()
                and municipality.is_enabled()
                and location.is_enabled())
                 
            # Extra
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/ul/li[4]/a').click()

                # Marital status
                select_marital_status = driver.find_element_by_xpath('//*[@id="t-hist-ext"]/div/div/select')
                select_marital_status.send_keys(estado_civil_h_c)

                # Number of children
                number_children = driver.find_element_by_xpath('//*[@id="t-hist-ext"]/div/div/input[1]')
                number_children.clear()
                number_children.send_keys(hijos_h_c)

                # Highest degree of studies
                degree_studies = driver.find_element_by_xpath('//*[@id="t-hist-ext"]/div/div/input[2]')
                degree_studies.clear() 
                degree_studies.send_keys(mx_estudios_h_c)

                # Occupation
                occupation = driver.find_element_by_xpath('//*[@id="t-hist-ext"]/div/div/input[3]')
                occupation.clear()
                occupation.send_keys(ocupacion_h_c)

                # Religion
                religion = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[4]/div/div/input[4]')
                religion.clear()
                religion.send_keys(religion_h_c)

                self.assertTrue(number_children.is_enabled()
                and degree_studies.is_enabled()
                and occupation.is_enabled()
                and religion.is_enabled())

            # System
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/ul/li[5]/a').click()

                # Digestive system
                digestive_system = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[5]/div/div[1]/textarea')
                digestive_system.clear()
                digestive_system.send_keys(sis_digestivo_h_c)

                # Musculoskeletal system
                musculoskeletal_system = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[2]/textarea')
                musculoskeletal_system.clear()
                musculoskeletal_system.send_keys(sis_musculo_h_c)

                # Neurological system
                neurological_system = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[3]/textarea')
                neurological_system.clear()
                neurological_system.send_keys(sis_neurologico_h_c)

                # Reproductive system
                reproductive_system = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[4]/textarea')
                reproductive_system.clear()
                reproductive_system.send_keys(sis_reproductor_h_c)

                # Respiratory system
                respiratory_system = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[5]/textarea')
                respiratory_system.clear()
                respiratory_system.send_keys(sistema_respi_h_c)

                # Senses system
                senses_system = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[6]/textarea')
                senses_system.clear()
                senses_system.send_keys(sis_de_sentidos_h_c)

                # Integumentary system
                integumentary_system  = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[7]/textarea')
                integumentary_system.clear()
                integumentary_system.send_keys(sis_tegumentario_h_c)

                # Urinary system
                urinary_system = driver.find_element_by_xpath('//*[@id="t-hist-sist"]/div/div[8]/textarea')
                urinary_system.clear()
                urinary_system.send_keys(sis_urinario_h_c)

                self.assertTrue(digestive_system.is_enabled()
                and musculoskeletal_system.is_enabled()
                and neurological_system.is_enabled()
                and reproductive_system.is_enabled()
                and respiratory_system.is_enabled()
                and senses_system.is_enabled()
                and integumentary_system.is_enabled()
                and urinary_system.is_enabled())
                
                # Update button
                button_update = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]')
                self.assertTrue(button_update.is_displayed())
                button_update.click()
                time.sleep(3)

                # # Button 1st close table
                # driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[1]/button').click()
                
                # Button 2do close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()

                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Actulizar historia clinica')) 
© 2022 GitHub, Inc.
Terms