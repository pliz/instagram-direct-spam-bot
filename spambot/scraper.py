import subprocess
import json
import time

def get_users_from_like( post, sessionid, count, start_from):
    command = f'''/usr/bin/node "/home/eagle/d/myapp/cassinelli/dir-spam-bot/spambot/scrape_post.js" "{post}" "{sessionid}" {count} {start_from}'''
    output = str(subprocess.check_output(command, shell=True)).replace("b'", "").replace("'", "")
    users_dict = json.loads(output)
    return users_dict


def pages_scraper(driver, page, req_number=50, start_from=1):
    first=True
    count_req = 0
    users_raw = []
    users= []
    next_page = ""
    users_scraped = 0
    change = 0
    driver.get(f"view-source:https://www.instagram.com/{page}/?__a=1")#get user id
    page_source = driver.page_source
    page_source = driver.find_element_by_tag_name("pre").text
    insta_id = (json.loads(page_source))["graphql"]["user"]["id"]
    req_number= req_number + start_from - 1
    req_number_final = None
    if req_number < 50:#se è mi9nore di 50 esegue solo uan richiesta 
        req_number_final = 1
    else:
        req_number_final = req_number//50#altiemnti calcola il numero di richieste
        change = req_number- (req_number_final*50)
        if change != 0:
            req_number_final+=1
        req_number_orginal = req_number
        req_number = 50
    if start_from==0:
        start_from=1
    for n in range(req_number_final):
        time.sleep(1.3)
        if first:
            print("prima richiesta")
            count_req +=1
            next_page = ""
            driver.get('''view-source:https://www.instagram.com/graphql/query/?query_hash=5aefa9893005572d237da5068082d8d5&variables={"id":"'''+ insta_id+'''","include_reel":false,"fetch_mutual":false,"first":'''+str(req_number)+'''}''')
            try:
                users_html = driver.page_source
                users_html = driver.find_element_by_tag_name("pre").text
                users_json = (json.loads(users_html))["data"]["user"]["edge_followed_by"]
                for user_raw in users_json["edges"]:
                    users_scraped+=1
                    if users_scraped >= start_from:
                        users_raw.append(user_raw)
                    else:
                        pass
                if users_json["page_info"]["has_next_page"]:
                    next_page = users_json["page_info"]["end_cursor"]
                else:
                    break
                first = False
                print(count_req)
                print(users_scraped)
            except Exception as error:
                print(error)
                print(count_req)
                continue
        elif (req_number_orginal-users_scraped)<=change or ((req_number_orginal-users_scraped)-change)<=5:
            count_req+=1
            print("gestione resto")
            driver.get('''view-source:https://www.instagram.com/graphql/query/?query_hash=5aefa9893005572d237da5068082d8d5&variables={"id":"'''+ insta_id+'''","include_reel":false,"fetch_mutual":false,"first":'''+str(change)+''',"after":"'''+next_page+'''"}''')
            try:
                users_html = driver.page_source
                users_html = driver.find_element_by_tag_name("pre").text
                users_json = (json.loads(users_html))["data"]["user"]["edge_followed_by"]
                for user_raw in users_json["edges"]:
                    users_scraped+=1
                    if users_scraped >= start_from:
                        users_raw.append(user_raw)
                    else:
                        pass
                if users_json["page_info"]["has_next_page"]:
                    next_page = users_json["page_info"]["end_cursor"]
                else:
                    break
                first = False
                print(count_req)
                print(users_scraped)
            except Exception as error:
                print(error)
                print(count_req)
                continue
        else:
            count_req+=1
            driver.get('''view-source:https://www.instagram.com/graphql/query/?query_hash=5aefa9893005572d237da5068082d8d5&variables={"id":"'''+ insta_id+'''","include_reel":false,"fetch_mutual":false,"first":50,"after":"'''+next_page+'''"}''')
            try:
                users_html = driver.page_source
                users_html = driver.find_element_by_tag_name("pre").text
                users_json = (json.loads(users_html))["data"]["user"]["edge_followed_by"]
                for user_raw in users_json["edges"]:
                    users_scraped+=1
                    if users_scraped >= start_from:
                        users_raw.append(user_raw)
                    else:
                        pass
                if users_json["page_info"]["has_next_page"]:
                    next_page = users_json["page_info"]["end_cursor"]
                else:
                    break
                first = False
                print(count_req)
                print(users_scraped)
            except Exception as error:
                print(error)
                print(count_req)
                continue
    final_users_list_count = 0
    for user in users_raw:
        user_node = user["node"]
        if not user_node["is_private"]:
            del user_node["profile_pic_url"]
            del user_node["followed_by_viewer"]
            del user_node["requested_by_viewer"]
            del user_node["follows_viewer"]
            users.append(user_node)
            final_users_list_count+=1
    print("parsed user... "+ str(final_users_list_count))
    return users


if __name__ == "__main__":
    print(get_users_from_like("https://www.instagram.com/p/CJVvrqyFFDM/", "sessionid=33953216539%3AaVkgkaZi49GKAe%3A27", "20", "0"))