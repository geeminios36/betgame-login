from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class Login:
    accounts = ['0528695750|T0ngnamm', '0984967115|anhkiem']
    videoUrl = 'https://tx.app611.net/Game/KULive.aspx?kuUrl=https://gat5.vn3kuvideo.com/'
    mainUrl = 'https://tx.app611.net/index.aspx'
    SCREENONE = 1
    SCREENTWO = 2

    def __init__(self):
        self.main()
        # self.getData()

    def main(self):
        browser = webdriver.Chrome()
        browser.get(self.mainUrl)

        self.loginWeb(browser, self.accounts[0])

        self.switchToWindow(browser, self.SCREENONE)

        print('Click to baccarat_btn')
        browser.find_element(By.CLASS_NAME, 'baccarat_btn').click()
        sleep(2)

        print('Getting source...')
        baccaratCn = browser.find_element(
            By.ID, 'scroll_pane').get_attribute('outerHTML')

        # start login again
        self.signOut(browser)
        self.loginWeb(browser, self.accounts[1])
        sleep(3)
        # end login again

        self.switchToWindow(browser, self.SCREENTWO)

        print('Click to BKbaccarat_btn')
        browser.find_element(By.CLASS_NAME, 'BKbaccarat_btn').click()
        sleep(2)

        print('Getting source...')
        baccaratMc = browser.find_element(
            By.ID, 'scroll_pane').get_attribute('outerHTML')

        print('==========================')
        print('Start clone data!')
        print('==========================')
        
        self.whileSave(baccaratCn, baccaratMc)

    def loginWeb(self, browser, account):
        account = account.split('|')
        print('Login account ' + account[0])

        browser.find_element(By.ID, 'txtUser').send_keys(account[0])
        browser.find_element(By.ID, 'txtPassword').send_keys(account[1])

        sleep(3)
        browser.find_element(By.CLASS_NAME, 'btn_signIn').click()
        
        sleep(5)

    def signOut(self, browser):
        print('Signing out...')
        browser.switch_to.window(browser.window_handles[0])
        browser.find_element(By.CLASS_NAME, 'btn_memSignOut').click()
        sleep(3)

    def switchToWindow(self, browser, screenNumber):
        print('Switch to window bet')
        browser.execute_script('window.open('');')
        browser.switch_to.window(browser.window_handles[screenNumber])
        browser.get(self.videoUrl)
        sleep(15)

    def whileSave(self, baccaratCn, baccaratMc):
        i = 0
        while (True):
            i = i+1
            try:
                self.saveData(baccaratCn, 'cn')
                self.saveData(baccaratMc, 'mc')
                seconds = 5
                while seconds:
                    mins, secs = divmod(seconds, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print("Sleeping in " + timer, end="\r")
                    time.sleep(1)
                    seconds -= 1
            finally:
                print('Crawler file successfully!')
            pass

    def saveData(self, source, type):
        self.append_new_line('./public/domHTML/'+type+".html", source)

    def append_new_line(self, file_name, source):
        with open(file_name, "wb") as file:
            file.write(source.encode())

if __name__ == "__main__":
    login = Login()
    login.loginWeb()
