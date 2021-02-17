from spambot.bot import Bot
from spambot.login import login
from spambot.scraper import pages_scraper
import argparse
import json
import time

send_message = 0
message_already_sent = 0
not_send_message = 0
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
            check_word = configuration["check_word"]
            sleep_time = configuration["time"]
            print("you choose..."+str(configuration["name"]))
            break
    if sleep_time:
        print("aspetto..."+ str(sleep_time))
        sleep_time = sleep_time * 60
        time.sleep(sleep_time)
    else:
        pass

    #inizializzazione driver con login
    try:
        personal_login = login(username, password)
        myuser = personal_login["driver"]
        current_sessionid = "sessionid="+personal_login["sessionid"]
    except Exception as error:
        print("error in login:")
        print(error)
        exit()

    #raccolta utenti
    try:
        users = pages_scraper(myuser, page_for_users, req_number=count, start_from=start_from, export=True)
        print("finish get users")
    except Exception as error:
        print(error)

    #inizializzazione bot
    message = str(message)
    if not check_word:
        print("not check")
        check_word=None
    bot = Bot(message,myuser, check=check_word)
    for user in users:
        try:
            print("starting send message...")
            start_time = time.time()
            message_status = bot.send(user["username"])
            if message_status == "send":
                send_message +=1
                print("send message...")
                print(send_message)
                print(time.time()-start_time)
            if message_status == "send-past":
                message_already_sent +=1
                print("gia mandati...")
                print(message_already_sent)
                print(time.time()-start_time)
        except Exception as error:
            not_send_message+=1
            print(error)
            print(not_send_message)
    total_time = time.time()-total_start_time
    total_message = send_message + not_send_message
    print("messagi totali: "+str(total_message)+
    "\nmessagi inviati: "+str(send_message)+
    "\nutenti saltati perchè gia mandati: "+str(message_already_sent)+
    "\nmessagi non inviati: "+str(not_send_message)+
    "\ntotal time: "+str(total_time)
    )


