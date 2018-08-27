from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request    


starttime=time.time()
while True:

    
    browser = webdriver.Firefox(executable_path='/home/marcus/Hämtningar/geckodriver')

    browser.get('http://192.168.1.1')

    elem = browser.find_element_by_id("txt_Username")  # Find the search box

    elem.send_keys(Keys.RETURN + 'admin')
    elem = browser.find_element_by_id("txt_Password")  # Find the search box

    elem.send_keys(Keys.RETURN + 'admin')

    elem = browser.find_element_by_id("login_btn").click()
    #elem.send_keys(Keys.RETURN)
    time.sleep(5)
    elem = browser.find_element_by_id("Admin_0_5").click()
    time.sleep(5)
    elem = browser.find_element_by_id("Admin_0_5_1").click()
    time.sleep(5)

    elem = browser.find_element_by_id("phnoe_number")
    elem.send_keys(Keys.RETURN + '72661')
    elem = browser.find_element_by_id("sms_msg_content")
    elem.send_keys(Keys.RETURN + 'TOPUP')
    time.sleep(5)
    elem = browser.find_element_by_id("sendBtn").click()
    time.sleep(10)
    elem = browser.find_element_by_id('delete_tr_btn').click()
    time.sleep(5)
    elem = browser.switch_to_alert().accept()
    time.sleep(5)
    elem = browser.find_element_by_id('sentbox_tr_btn').click()
    time.sleep(10)
    elem = browser.find_element_by_id('delete_tr_btn').click()
    time.sleep(5)
    elem = browser.switch_to_alert().accept()
    browser.quit()


    time.sleep(60.0 - ((time.time() - starttime) % 60.0))