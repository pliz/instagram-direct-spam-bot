# made by Nicolò Valenza
# 22 03 2020
# client desktop per il modulo instagram-driect-spam-bot
import tkinter as tk
import json
import time
import os
os.chdir("/home/eagle/d/myapp/cassinelli/dir-spam-bot-client-desktop")


class App:
    def __init__(self, filename, tk):
        self.tk = tk
        self.window = self.tk.Tk()  # inizio classe tkinter
        self.filename = filename
        # apertura file json per salvatggio account
        self.accounts_list = self.get_json_datas(self.filename)
        self.window.title("instagram spam bot")
        self.is_editing = False
        self.init_app_home()
        self.window.mainloop()  # inizio ciclo app

    def get_json_datas(self, filename):
        with open(filename) as config_file:
            accounts_list = json.load(config_file)
            return accounts_list

    def init_app_home(self):  # questa funzione inizia la home dell'app
        row_frame = 0
        for account in self.accounts_list:  # per ogni account mostar i dati
            row_n = 0
            new_frame = self.tk.Frame(master=self.window)
            new_frame.grid(row=row_frame, column=0)
            name = "nome = " + str(account["name"])
            username = "username = "+str(account["username"])
            password = "password = "+str(account["password"])
            count = "messaggi da mandare = " + str(account["count"])
            start_from = "messaggi mandati prima = " + str(account["start_from"])
            source_page = "pagina da cui prendere gli utenti = " + str(account["users_page"])
            check_word = "parola da controllare = " + str(account["check_word"])
            finish = ""
            c = 0
            for char in account["message"]:
                if c== 50:
                    c = 0
                    finish += "\n"
                finish += char
                c+=1
            message = "messaggio da mandare = \n" + str(finish)
            name_view = self.tk.Label(master=new_frame, text=name)
            name_view.grid(row=row_n, column=0)
            row_n += 1
            username_view = self.tk.Label(master=new_frame, text=username)
            username_view.grid(row=row_n, column=0)
            row_n += 1
            password_view = self.tk.Label(master=new_frame, text=password)
            password_view.grid(row=row_n, column=0)
            row_n += 1
            count_view = self.tk.Label(master=new_frame, text=count)
            count_view.grid(row=row_n, column=0)
            row_n += 1
            start_from_view = self.tk.Label(master=new_frame, text=start_from)
            start_from_view.grid(row=row_n, column=0)
            row_n += 1
            page_view = self.tk.Label(master=new_frame, text=source_page)
            page_view.grid(row=row_n, column=0)
            row_n += 1
            check_word_view = self.tk.Label(master=new_frame, text=check_word)
            check_word_view.grid(row=row_n, column=0)
            row_n += 1
            message_view = self.tk.Label(master=new_frame, text=message)
            message_view.grid(row=row_n, column=0)
            row_n += 1
            button_get_user = self.tk.Button(master=new_frame, text="edit", command=lambda arg1=str(
                account["name"]), frame=new_frame, row=(row_n+1): self.get_edit_account(arg1, frame, row))
            button_get_user.grid(row=row_n, column=0)
            row_frame += 1

    def get_edit_account(self, name, frame, start_row):
        print(name)
        if not self.is_editing:
            self.is_editing = True
            for account in self.accounts_list:
                if account["name"] == name:
                    form = self.tk.Toplevel(master=frame)
                    form_row = 0
                    name_view = self.tk.Label(master=form, text="edit")
                    name_view.grid(row=form_row, column=0)
                    form_row += 1
                    username_entry = self.tk.Entry(master=form)  # 0
                    username_entry.insert(0, str(account["username"]))
                    username_entry.grid(row=form_row, column=0)
                    form_row += 1
                    password_entry = self.tk.Entry(master=form)  # 1
                    password_entry.insert(0, str(account["password"]))
                    password_entry.grid(row=form_row, column=0)
                    form_row += 1
                    count_entry = self.tk.Entry(master=form)  # 2
                    count_entry.insert(0, str(account["count"]))
                    count_entry.grid(row=form_row, column=0)
                    form_row += 1
                    start_from_entry = self.tk.Entry(master=form)  # 4
                    start_from_entry.insert(0, str(account["start_from"]))
                    start_from_entry.grid(row=form_row, column=0)
                    form_row += 1
                    source_page_entry = self.tk.Entry(master=form)  # 5
                    source_page_entry.insert(0, str(account["users_page"]))
                    source_page_entry.grid(row=form_row, column=0)
                    form_row += 1
                    check_word_entry = self.tk.Entry(master=form)  # 6
                    check_word_entry.insert(0, str(account["check_word"]))
                    check_word_entry.grid(row=form_row, column=0)
                    form_row += 1
                    message_entry = self.tk.Entry(master=form)  # 7
                    message_entry.insert(0, str(account["message"]))
                    message_entry.grid(row=form_row, column=0)
                    form_row += 1
                    button_submit = self.tk.Button(master=form, text="submit", command=lambda arg1=form,
                     name=name, 
                     username=username_entry,
                     password=password_entry,
                     count=count_entry,
                     start_from=start_from_entry,
                     source_page=source_page_entry,
                     check_word=check_word_entry,
                     message=message_entry
                     : self.close_edit_window(form, name,username,  password, count, start_from, source_page, check_word, message))
                    button_submit.grid(row=form_row, column=0)
                    break

    def close_edit_window(self, window, name, username, password, count, start_from, source_page, check_word, message):
        self.is_editing = False
        for account in self.accounts_list:
            if account["name"] == name:
                element_list_index = self.accounts_list.index(account)
                self.accounts_list[element_list_index]["username"] = str(username.get())
                self.accounts_list[element_list_index]["password"] = str(password.get())
                self.accounts_list[element_list_index]["count"] = int(count.get())
                self.accounts_list[element_list_index]["start_from"] = int(start_from.get())
                self.accounts_list[element_list_index]["users_page"] = str(source_page.get())
                self.accounts_list[element_list_index]["check_word"] = str(check_word.get())
                self.accounts_list[element_list_index]["message"] = str(message.get())
        with open(self.filename, "w") as file:
            json.dump(self.accounts_list, file)
        window.destroy()
        self.window.destroy()
        self.__init__(self.filename, self.tk)


if __name__ == "__main__":
    App("/home/eagle/d/myapp/cassinelli/dir-spam-bot-client-desktop/config.json", tk)
