import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv
import time
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class ShowStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        
    #unit tests  
    def test_schedule_branch(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.maximize_window()
        driver.implicitly_wait(1)
      
        lista = []
        with open('agenda_estudio.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
           
        x=0
        for linea in lista:
            if(x==0):
                x=x+1
            else:
                correo = linea [0]
                contrasenia = linea [1]
                estudios = linea [2]
                estados = linea [3]
                ciudad = linea [4]
                sucursal = linea [5]
                fecha_prue = linea[6]

                driver.find_element_by_xpath('//*[@id="flipkart-navbar"]/div/div[2]/div[3]/a').click()

            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')

                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)

                input = driver.find_element_by_css_selector('body > ngb-modal-window > div > div > div.modal-body > div > form > div > div > div > div:nth-child(1) > button')
                input.click()
                driver.implicitly_wait(2)

                close = driver.find_element_by_css_selector('body > ngb-modal-window > div > div > div.modal-header > button')
                close.click()

                driver.implicitly_wait(1)

                select_state = Select(driver.find_element_by_name('estados'))
                select_state.select_by_visible_text(estados)
                
                driver.implicitly_wait(1)
                select_city = Select(driver.find_element_by_name('ciudades'))
                select_city.select_by_visible_text(ciudad)
                
                driver.implicitly_wait(1)
                study = driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[2]/div[2]/div/input')
                study.send_keys(estudios)

                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[2]/div[2]/div/button').click()
                
                # select laboratory
                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[4]/div/section/div[2]/div/div[1]/div/div[1]/div/div/button[2]').click()

                # next first
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[2]/button').click()              

                #next second
                select_type_quote = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[4]/select'))
                time.sleep(1)

                # type quote
                # select_type_quote.select_by_visible_text('Cita Agendada')
                #third next
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[4]/button[2]').click()
                time.sleep(1)

                #Choose a branch
                select_office = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[6]/div/select'))
                # select_office = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "inlineFormCustomSelect")))
                select_office.select_by_visible_text(sucursal)
                time.sleep(1)
                
                #Fourth next
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[6]/button[2]').click()

                # Select the day 
                date = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[8]/div/form/input')
                date.send_keys(fecha_prue)

                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[8]/div/button').click()

                # select hour
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div/div[1]/div/div/blockquote/h4').click()
                
                # fifth next
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[8]/button[2]').click()
                time.sleep(1)

                # Select the schedule
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div[10]/div[3]/button[2]').click()
                time.sleep(1)

                #Add shopping cart
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-carrito/html/body/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/button').click()
                time.sleep(1)

                #Get out
                driver.find_element_by_xpath('/html/body/app-root/div/app-menu-estudios/html/body/div/div/app-navbar/div/div[1]/div[2]/nav/ul/li[6]/div/a[1]').click()

             
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Agendar_en_sucursal'))
