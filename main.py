from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.options import Options
import time
import json

HEADLESS=False#don't set to True
MESSAGE = ''''''#enter message
USERNAME = ""#enter username
PASSWORD = ""#enter password

count = 0

class Bot:
    def __init__(self, message, driver):
        self.message = message
        self.driver = driver
    def send_in_dir(self):#questa funzione manda il messaggio
        driver = self.driver
        time.sleep(3)    
        messagelabel = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        messagelabel.send_keys(self.message)#selezione label di inseriemto e inserimeto del testo
        send_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")#selezione pulsante per invio
        send_button.click()#click sul pulsante
        print("send")
    def send(self, passed_user):
        driver = self.driver
        user = passed_user#ricevenet
        driver.get(f"https://www.instagram.com/{user}")#apertura profilo ricevente
        try:
            time.sleep(1)
            driver.execute_script('''document.querySelector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button").click()''')
            '''selezione pulsante con javascript e iscrizione al utente'''
        except Exception as errror:
            print(errror)
        time.sleep(2)
        driver.execute_script('''document.querySelector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div._862NM > div > button").click()''')
        try:
            self.send_in_dir()#manda il messaggio
        except ElementClickInterceptedException:
            time.sleep(5)
            self.send_in_dir()
        time.sleep(1)
        driver.get(f"https://www.instagram.com/{user}")#ritorna allla pagina del ricevente
        time.sleep(1)
        try:
            driver.execute_script('''document.querySelector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div:nth-child(2) > div > span > span.vBF20._1OSdk > button").click()''')
            time.sleep(0.3)
            driver.execute_script('''document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.-Cab_").click()''')
            '''esecuzuione script javascript che si disiscrive dal utente'''
            time.sleep(0.5)
        except Exception as errror:
            print(errror)
        
def login(headless, username, password):
    myoptions = Options()
    myoptions.headless = headless
    driver = webdriver.Firefox(options=myoptions)
    driver.get("https://instagram.com")
    time.sleep(1)
    driver.execute_script('''document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR").click()''')
    time.sleep(2)
    username_inp = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    username_inp.send_keys(username)
    time.sleep(2)
    password_inp = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password_inp.send_keys(password)
    time.sleep(2)
    driver.execute_script('''document.querySelector("#loginForm > div > div:nth-child(3) > button").click()''')
    time.sleep(6)
    driver.execute_script('''document.querySelector("#react-root > section > main > div > div > div > section > div > button").click()''')
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
    time.sleep(3)
    
    return driver

if __name__ == "__main__":
    try:
        driver = login(HEADLESS, USERNAME, PASSWORD)
    except Exception as errror:
        print("error in login:")
        print(errror)
        exit()
   
    with open("user.json") as users_list_file:
        global users_list
        users_list = json.load(users_list_file)
    bot = Bot(MESSAGE, driver)
    for user in users_list:
        count+=1
        print(count)
        try:
            bot.send(user["username"])
        except Exception as errror:
            print(errror)
            pass
    print("finish")
    driver.quit()
    exit()