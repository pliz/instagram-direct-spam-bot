from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time
import json
MESSAGE = "test"
class Bot:
    def __init__(self, message):
        self.message = message
    def send_in_dir(self):#questa funzione manda il messaggio
        time.sleep(1)    
        messagelabel = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        messagelabel.send_keys(self.message)#selezione label di inseriemto e inserimeto del testo
        send_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")#selezione pulsante per invio
        send_button.click()#click sul pulsante
        print("send")
    def send(self, passed_user):
        user = passed_user#ricevenet
        driver.get(f"https://www.instagram.com/{user}")#apertura profilo ricevente
        try:
            time.sleep(2)
            driver.execute_script('''document.querySelector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button").click()''')
            '''selezione pulsante con javascript e iscrizione al utente'''
        except Exception as errror:
            print(errror)
        time.sleep(1)
        open_user_direct_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")#selezione pulsante apertura direct
        open_user_direct_button.click()#apertura client direct
        try:
            self.send_in_dir()#manda il messaggio
        except ElementClickInterceptedException:
            time.sleep(5)
            self.send_in_dir()
        time.sleep(1)
        driver.get(f"https://www.instagram.com/{user}")#ritorna allla pagina del ricevente
        time.sleep(1)
        try:
            driver.execute_script('''document.querySelector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div:nth-child(2) > div > span > span.vBF20._1OSdk > button").click();document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.-Cab_").click()''')
            '''esecuzuione script javascript che si disiscrive dal utente'''
        except Exception as errror:
            print(errror)
        


driver = webdriver.Firefox()
driver.get("https://instagram.com")

while True:
    action = input("...")
    bot = Bot(MESSAGE)
    if action=="s":
        bot.send("cassinellimarco.official")
    elif action== "b":
        break
    else:
        print("boh")


# while open("user.json") as users_list_file:
#     global users_list
#     users_list = json.load(users_list_file)
# bot = Bot(MESSAGE)
# for user in users_list:
#     bot.send(user["username"])
