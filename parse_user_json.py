import json
import os
RAW_FILE_NAME = "user_raw.json"
FILE_NAME = "user.json"
public_users_list = []
os.system("node gen_raw_user.js")#creazione file con utenti
with open(RAW_FILE_NAME) as users_raw:#apertura del file con gli utenti forniti da instatouch
    global dict_users_raw
    dict_users_raw= json.load(users_raw)#salvataggio degli untenti in un dizionario
for user in dict_users_raw:#per ogni utente
    if not user["is_private"]:#se non è privato
        del user["id"]# elliminazione dati non necessari 
        del user["profile_pic_url"]
        public_users_list.append(user)#aggiunta alla lista
clear_final_file = open(FILE_NAME, "w")
clear_final_file.write(json.dumps(public_users_list))#salvataggio file
clear_final_file.close()

