import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def login(username, password, headless=True):
    print("start login")
    profile = webdriver.FirefoxProfile()
    # authorize notificatrion
    profile.set_preference('permissions.default.desktop-notification', 1)
    myoptions = Options()
    myoptions.headless = headless  # activate headless mode

    driver = webdriver.Firefox(
        options=myoptions, firefox_profile=profile)  # open browser
    driver.get("https://instagram.com")
    time.sleep(1)
    driver.execute_script('''
    document.querySelector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR").click()
    ''')# accept cookies  
    time.sleep(2)
    username_inp = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")#insert username
    username_inp.send_keys(username)
    time.sleep(2)
    password_inp = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")#insert password
    password_inp.send_keys(password)
    time.sleep(2)
    driver.execute_script(
        '''document.querySelector("#loginForm > div > div:nth-child(3) > button").click()''')#submit credentials
    
    time.sleep(6)
    try:#se trova il rpompt che chiede di salvare le credenziali lo accetta
        driver.execute_script(
'''document.querySelector("#react-root > section > main > div > div > div > section > div > button").click()''')#save credentials
    except Exception as error:
        print("message not found")
    print("login finish")
    time.sleep(7)
    for cookie in driver.get_cookies():#get session id from cookie
        if cookie["name"] == "sessionid":
            sessionid = cookie["value"]
            break
    return {"driver": driver, "sessionid": sessionid}