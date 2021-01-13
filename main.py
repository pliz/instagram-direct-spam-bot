from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.options import Options
import time
import json
HEADLESS=False
count = 0
MESSAGE = '''Ciao, ho visto che sei molto interessato/a a giochi tipo ROBLOX, CLASH ROYALE, BRAWL STARS, ecc. 🎮Noi di @123_black.galaxy abbiamo da poco aperto un canale DISCORD e siamo molto interessati a tutti questi giochi 🎯. Se entri e ci aiuti a gestire il server, anche ovviamente GIOCANDO con altre persone, potremmo darti un ruolo importante sul server e in futuro potresti essere uno dei CAPI della community che si sta INGRANDENDO molto RAPIDAMENTE 👑💸. Se sei interessato/a a partecipare contattaci in PRIVATO o clicca il LINK nella BIO di 123_black.galaxy per entrare nel server 📈🇮🇹'''
class Bot:
    def __init__(self, message):
        self.message = message
    def send_in_dir(self):#questa funzione manda il messaggio
        time.sleep(3)    
        messagelabel = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        messagelabel.send_keys(self.message)#selezione label di inseriemto e inserimeto del testo
        send_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")#selezione pulsante per invio
        send_button.click()#click sul pulsante
        print("send")
    def send(self, passed_user):
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
            time.sleep(0.2)
        except Exception as errror:
            print(errror)
        
myoptions = Options()
myoptions.headless = HEADLESS
driver = webdriver.Firefox(options=myoptions)
driver.get("https://instagram.com")

# while True:
#     action = input("...")
#     bot = Bot(MESSAGE)
#     if action=="s":
#         bot.send("cassinellimarco.official")
#     elif action== "b":
#         break
#     else:
#         print("boh")
for n in range(40):
    time.sleep(1)
    print(n+1)

with open("user.json") as users_list_file:
    global users_list
    users_list = json.load(users_list_file)
bot = Bot(MESSAGE)
for user in users_list:
    count+=1
    print(count)
    try:
        bot.send(user["username"])
    except Exception as errror:
        print(errror)
        pass

driver.quit()