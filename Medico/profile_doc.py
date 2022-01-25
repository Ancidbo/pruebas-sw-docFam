import unittest
import csv, operator
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class ProfileDoctor(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_profile_doctor(self):
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
                # tipo_cita = linea [4]
                # costo = linea [5]
                # fecha = linea [6]
                # hora_i = linea [7]
                # hora_f = linea [8]
                # telefono = linea [9]
                # nombre_pacinte = linea [10]
                # apellido_p_paciente = linea[11]
                # apellido_m_paciente = linea [12]
                # correo_paciente = linea [13]
                # telefono_paciente = linea [14]
                # fecha_nacimeitno_paciente = linea[15]               
                # sexo_paciente = linea[16]
                # contrasena_paciente = linea [17]
                especialidad = linea [18]
                sub_especialidad = linea [19]
                sexo_medico = linea [20]
                fecha_nacimiento_medico = linea [21]
                telefono_medico = linea [22]
                estado_actual_medico = linea [23]
                calle_medico = linea [24]
                colonia_medico = linea [25]
                numero_inte_medico = linea [26]
                numero_exterior_medico = linea [27]
                cp_medico = linea [28]
                municipio_medico = linea [29]
                localidad_medico = linea [30]
                decripcion_medico = linea [31]             

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
                # Button profile
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[5]').click()

                # Button update data
                driver.find_element_by_xpath('//*[@id="container-princ"]/app-medico-perfil/div/div/div/div[2]/button[2]').click()

            # Update
                # General
                # Specialty
                specialty = Select(driver.find_element_by_xpath('//*[@id="t-med-gral"]/select[1]')) 
                specialty.select_by_visible_text(especialidad)

                # Sub Specialty
                sub_specialty = driver.find_element_by_xpath('//*[@id="t-med-gral"]/textarea')
                sub_specialty.clear()
                sub_specialty.send_keys(sub_especialidad)

                # Sex
                select_sex = Select(driver.find_element_by_id('sexo')) 
                select_sex.select_by_visible_text(sexo_medico)

                # Born
                born = driver.find_element_by_id('date')
                born.clear()
                born.send_keys(fecha_nacimiento_medico)

                # Phone
                phone =  driver.find_element_by_xpath('//*[@id="t-med-gral"]/input[2]')
                phone.clear()
                phone.send_keys(telefono_medico)

                # State
                select_state = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/div[1]/select[3]')) 
                select_state.select_by_visible_text(estado_actual_medico)
                
                self.assertTrue(sub_specialty.is_enabled() 
                and born.is_enabled()
                and phone.is_enabled())
                

            # Consulting room
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/ul/li[2]/a').click()

                # Street
                street = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[1]')
                street.clear()
                street.send_keys(calle_medico)

                # Suburb
                suburb = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[2]')
                suburb.clear()
                suburb.send_keys(colonia_medico)

                # Interior number
                interior_number = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[3]')
                interior_number.clear()
                interior_number.send_keys(numero_inte_medico)

                # Outdoor Number
                outdoor_number = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[4]')
                outdoor_number.clear()
                outdoor_number.send_keys(numero_exterior_medico)

                # Cp
                cp = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[5]')
                cp.clear()
                cp.send_keys(cp_medico)

                # Municipality
                municipality = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[6]')
                municipality.clear()
                municipality.send_keys(municipio_medico )
                
                # Location
                location = driver.find_element_by_xpath('//*[@id="t-med-cons"]/input[7]')
                location.clear()
                location.send_keys(localidad_medico)
                
                self.assertTrue(street.is_enabled() 
                and suburb.is_enabled()
                and interior_number.is_enabled()
                and outdoor_number.is_enabled()
                and cp.is_enabled()
                and municipality.is_enabled()
                and location.is_enabled())

            # Description
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/ul/li[3]/a').click()
            
                # Text Description
                description = driver.find_element_by_xpath('//*[@id="t-med-desc"]/textarea')
                description.clear()
                description.send_keys(decripcion_medico)

                self.assertTrue(description.is_enabled()) 

                # Button Update
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/button').click()
                    
                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()
                
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Actulizar datos de perfil')) 