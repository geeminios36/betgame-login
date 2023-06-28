
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class Login:
    def __init__(self):
        
        self.loginWeb()
        # self.getData()

    def loginWeb(self): 
        usernameStr = 'GEEMINIOS'
        passwordStr = 'T0ngnamm'

        browser = webdriver.Chrome()
        # browser.get(('https://vn2.ku6122.net'))
        browser.get(('https://tx.app611.net/index.aspx'))

        # sleep(3)
        # browser.find_element(By.ID, "loginbutton").click();
        # sleep(5)
        username = browser.find_element(By.ID, "txtUser")
        # username = browser.find_element(By.ID, "accountId")
        username.send_keys(usernameStr)

        password = browser.find_element(By.ID, "txtPassword")
        # password = browser.find_element(By.ID, "accountPwd")
        password.send_keys(passwordStr)

        # signInButton = browser.find_element(By.ID, "signin")
        signInButton = browser.find_element(By.CLASS_NAME, "btn_signIn")
        signInButton.click()

        sleep(5)
        browser.execute_script("window.open('');")
        # 
        browser.switch_to.window(browser.window_handles[1])
        # browser.get(('https://tx.app611.net/Game/KULive.aspx'))
        browser.get(('https://vn2.ku6122.net/CheckGame?gameType=BB_LiveGame&subGameType=&dt='+usernameStr+time.time()))
        # # browser.execute_script('''window.open("https://tx.app611.net/Game/KULive.aspx?kuUrl=https://gat5.vn3kuvideo.com/", "_blank");''')
        # sleep(10)
        # browser.find_element(By.CLASS_NAME, "flagshipNav_btn").click()
        # sleep(3)

        # #start login again
        # browser.switch_to.window(browser.window_handles[0])
        # browser.find_element(By.CLASS_NAME, "btn_memSignOut").click()
        # sleep(3)
        # browser.find_element(By.ID, "txtUser").send_keys(usernameStr)
        # browser.find_element(By.ID, "txtPassword").send_keys(passwordStr)
        # browser.find_element(By.CLASS_NAME, "btn_signIn").click()
        # #end login again

        # browser.execute_script("window.open('');")
        # browser.switch_to.window(browser.window_handles[2])
        # # browser.execute_script('''window.open("https://tx.app611.net/Game/KULive.aspx?kuUrl=https://gat5.vn3kuvideo.com/", "_blank");''')
        # browser.get("https://tx.app611.net/Game/KULive.aspx")
        # sleep(10)   
        # # browser.find_element(By.CLASS_NAME, "baccarat_btn").click()
        # # sleep(3)
   
        i=0
        while(True):
            i=i+1
            try: 
                print('incoming')
                # scrollPane = browser.find_element(By.ID, "scroll_pane").text
                # scrollPane = browser.find_element(By.ID, "scroll_pane")
                # if scrollPane:
                #     source_code = scrollPane.get_attribute("outerHTML")
                #     self.getData(source_code)

            finally:
                print('not found')
                
            # sleep(10)
            sleep(5)
            pass

    def getData(self, source): 
        soup = BeautifulSoup(source, "html.parser")

        elements = soup.find_all("div", class_="game_box".split())
        print(elements)

        # print("\n".join("{} {}".format(el['class'], el.get_text()) for el in elements))
        

if __name__ == "__main__":
    login = Login()
    login.loginWeb()
