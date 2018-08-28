from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request    


starttime=time.time()
while True:
    def sms_func():
        
        browser = webdriver.Firefox(executable_path='./geckodriver')

        browser.get('http://192.168.1.1')

        elem = browser.find_element_by_id("txt_Username")

        elem.send_keys(Keys.RETURN + 'admin')
        elem = browser.find_element_by_id("txt_Password")

        elem.send_keys(Keys.RETURN + 'admin')

        elem = browser.find_element_by_id("login_btn").click()
        time.sleep(10)
        elem = browser.find_element_by_id("Admin_0_5").click()
        time.sleep(10)
        elem = browser.find_element_by_id("Admin_0_5_1").click()
        time.sleep(10)

        
        elem = browser.page_source
        with open('sms', 'w') as f:
            f.write(elem)
        with open('sms', 'r') as f:
            sms = f.readlines()[216][170:296]
            if sms == "Bra surfat! Vill du fortsätta? Svara TOPUP så kommer ytterligare 5 GB att surfa för. You've got the power 2 stay online! Tele2":
                elem = browser.find_element_by_id("phnoe_number")
                elem.send_keys(Keys.RETURN + '72661')
                elem = browser.find_element_by_id("sms_msg_content")
                elem.send_keys(Keys.RETURN + 'TOPUP')
                time.sleep(10)
                elem = browser.find_element_by_id("sendBtn").click()
                time.sleep(10)
                elem = browser.find_element_by_id('delete_tr_btn').click()
                time.sleep(10)
                elem = browser.switch_to_alert().accept()
                time.sleep(10)
                elem = browser.find_element_by_id('sentbox_tr_btn').click()
                time.sleep(10)
                elem = browser.find_element_by_id('delete_tr_btn').click()
                time.sleep(10)
                elem = browser.switch_to_alert().accept()
                browser.quit()
                sms_func()
            else:
                browser.quit()


    sms_func()
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))