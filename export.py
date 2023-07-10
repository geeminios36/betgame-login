from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import glob  # get the path of files
import time

from sendMsgTelegram import sendMsgTelegram


class Login:
    accounts = ['0528695750|T0ngnamm', '0984967115|anhkiem']
    videoUrl = 'https://tx.app611.net/Game/KULive.aspx?kuUrl=https://gat5.vn3kuvideo.com/'
    mainUrl = 'https://tx.app611.net/index.aspx'
    SCREENONE = 1
    SCREENTWO = 2

    def __init__(self):
        self.main()


    def main(self):
        browser = webdriver.Chrome()
        browser.get(self.mainUrl)

        self.loginWeb(browser, self.accounts[0])

        self.switchToWindow(browser, self.SCREENONE)

        sleep(2)

        self.whileSave(browser)

        # start login again
        # self.signOut(browser)
        # browser = webdriver.Chrome()
        # browser.get(self.mainUrl)

        # self.loginWeb(browser, self.accounts[1])
        # sleep(3)
        # # end login again

        # self.switchToWindow(browser, self.SCREENTWO)

        # print('Click to BKbaccarat_btn')
        # browser.find_element(By.CLASS_NAME, 'BKbaccarat_btn').click()
        # sleep(2)

        # print('Getting source...')
        # baccaratMc = browser.find_element(
        #     By.ID, 'scroll_pane').get_attribute('outerHTML')

        # print('==========================')
        # print('Start clone data!')
        # print('==========================')

        # self.whileSave(baccaratMc, 'mc')

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

    def whileSave(self, browser):
        i = 0
        while (True):
            i = i+1
            try:
                browser.find_element(By.CLASS_NAME, 'baccarat_btn').click()
                baccarat = browser.find_element(
                    By.ID, 'scroll_pane').get_attribute('outerHTML')
                self.saveData(baccarat, 'cn')
                sleep(2)

                browser.find_element(By.CLASS_NAME, 'BKbaccarat_btn').click()
                baccarat = browser.find_element(
                    By.ID, 'scroll_pane').get_attribute('outerHTML')
                self.saveData(baccarat, 'blockchain')
                sleep(2)

                browser.find_element(By.CLASS_NAME, 'flagshipNav_btn').click()
                baccarat = browser.find_element(
                    By.ID, 'scroll_pane').get_attribute('outerHTML')
                self.saveData(baccarat, 'mc')

                self.copyToOneFile()


                telegramBot = sendMsgTelegram()
                telegramBot.sendToTelegram('Test bot send notification')
                seconds = 5

                while seconds:
                    mins, secs = divmod(seconds, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print('Sleeping in ' + timer, end='\r')
                    time.sleep(1)
                    seconds -= 1
            finally:
                print('==========================>')
            pass

    def saveData(self, source, type):
        self.append_new_line(type+'.txt', source)

    def append_new_line(self, file_name, source):
        with open(file_name, 'wb') as file:
            file.write(source.encode())

    def copyToOneFile(self):
        file_to_delete = open("index.html", 'w')
        file_to_delete.close()

        with open("index.html", 'a') as csv_file:
            for path in glob.glob('./*.txt'):
                with open(path) as txt_file:
                    txt = txt_file.read() + '\n'
                    csv_file.write(txt)


if __name__ == '__main__':
    login = Login()
    login.loginWeb()
