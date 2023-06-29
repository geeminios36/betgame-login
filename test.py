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
        usernameStr = 'develop'
        passwordStr = '12345'

        browser = webdriver.Chrome()
        browser.get(('http://127.0.0.1:8000/'))

        username = browser.find_element(By.ID, "inputEmail")
        username.send_keys(usernameStr)

        password = browser.find_element(By.ID, "inputPassword")
        password.send_keys(passwordStr)

        signInButton = browser.find_element(By.CLASS_NAME, "btn-login")
        signInButton.click()

        sleep(5)
        browser.execute_script("window.open('');")

        browser.switch_to.window(browser.window_handles[1])
        browser.get(('http://127.0.0.1:8000/user'))
        sleep(5)   
        a = browser.find_element(By.ID, "datatable_user_wrapper").get_attribute("outerHTML")
        
        # #start login again
        browser.switch_to.window(browser.window_handles[0])
        browser.get(('http://127.0.0.1:8000/logout'))
        sleep(3)

        browser.find_element(By.ID, "inputEmail").send_keys(usernameStr)
        browser.find_element(By.ID, "inputPassword").send_keys(passwordStr)
        browser.find_element(By.CLASS_NAME, "btn-login").click()
        #end login again
        sleep(4)

        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[2])
        # # browser.execute_script('''window.open("https://tx.app611.net/Game/KULive.aspx?kuUrl=https://gat5.vn3kuvideo.com/", "_blank");''')
        browser.get("http://127.0.0.1:8000/bot")
        sleep(5)   
        b = browser.find_element(By.ID, "datatable_bot_wrapper").get_attribute("outerHTML")
        # sleep(10)   
   
        i=0
        while(True):
            i=i+1
            try: 
                print('incoming ')
                self.getData(a, 'cn')
                self.getData(b, 'mc')
                # print('incoming b', b)
                # scrollPane = browser.find_element(By.ID, "datatable_keeper").text
                # scrollPane = browser.find_element(By.ID, "scroll_pane")
                # if scrollPane:
                #     source_code = scrollPane.get_attribute("outerHTML")
                #     self.getData(source_code)

            finally:
                print('not found')
                
            # sleep(10)
            sleep(5)
            pass

    def getData(self, source, type): 
        # page = requests.get(url)
        self.append_new_line('./public/domHTML/'+type+".html", source)
        # with open("saving.html", "wb") as file:
        #     file.write(source.encode())
        # with open('../saving.html', 'wb+') as f:
        #     f.write(source.encode())
        # soup = BeautifulSoup(source, "html.parser")
        # elements = soup.find_all("div", class_="game_box".split())
        # print(elements)

        # print("\n".join("{} {}".format(el['class'], el.get_text()) for el in elements))

    def append_new_line(self, file_name, source):
        with open(file_name, "wb") as file:
            file.write(source.encode())
        
        # script = open('index.js', "r+")
        # file = open(file_name, "a")
        # file.write("\n")
        # file.write("<script>"+script.read()+"</script>")


if __name__ == "__main__":
    login = Login()
    login.loginWeb()
