from spambot.bot import Bot
from spambot.login import login
from spambot.scraper import pages_scraper
import argparse
import json
import time

send_message = 0
if __name__ == "__main__":
    total_start_time = time.time()
    with open("config.json", "r") as config:
        config_dict = json.load(config)

    for configuration in config_dict:
        print(str(config_dict.index(configuration)) + " "+ configuration["name"])

    config_to_use = int(input("chose configuration..."))
    for configuration in config_dict:
        if config_dict.index(configuration)==config_to_use:
            username = configuration["username"]
            password = configuration["password"]
            count = configuration["count"]
            start_from = configuration["start_from"]
            page_for_users= configuration["users_page"]
            message = configuration["message"]
            print("you choose..."+str(configuration["name"]))
            break
    try:
        personal_login = login(username, password)
        myuser = personal_login["driver"]
        current_sessionid = "sessionid="+personal_login["sessionid"]
    except Exception as error:
        print(error)
    
    try:
        print(current_sessionid)
        users = pages_scraper(myuser, page_for_users, req_number=count, start_from=start_from)
        print("finish get users")
    except Exception as error:
        print(error)

    message = str(message)
    bot = Bot(message,myuser)
    for user in users:
        try:
            send_message += 1
            print("starting send message...")
            print(send_message)
            start_time = time.time()
            bot.send(user["username"])
            print("send message...")
            print(send_message)
            print(time.time()-start_time)
        except Exception as error:
            print(error)
    print(time.time()-total_start_time)


