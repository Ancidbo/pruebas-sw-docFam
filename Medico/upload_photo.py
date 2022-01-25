import unittest
import time
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class UploadPhoto(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_upload_photo(self):
        driver = self.driver
        driver.get('https://mydocfam.com/')
        driver.maximize_window()
        driver.window_handles
        driver.implicitly_wait(1)
      
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
                # original_window = driver

             # Share items
                driver.find_element_by_xpath('/html/body/app-root/div/app-inicio/div[1]/div/div[1]/div[2]/a[1]').click()

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

                
                # profile
                driver.find_element_by_xpath('//*[@id="body"]/div[1]/div[2]/nav/ul/li[5]').click()

                driver.find_element_by_xpath('//*[@id="container-princ"]/app-medico-perfil/div/div/div/div[2]/button[1]').click()
                
                # Upload photo
                upload_photo = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div/div/input')
                upload_photo.send_keys('C:\\Users\\Semin\\Desktop\\medico\\descarga.jfif')
                
                # Button Upload 
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[2]').click()
                time.sleep(1)
                # Button close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
                
                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Subir_foto')) 