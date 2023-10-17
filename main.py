# This is a sample Python script.

import tkinter as tk
import json
import pandas as pd
import requests
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_specific_exchange_data(key='652dddec7e2b86.29923297', exchange = 'NYSE'):
    """
    just get details of specific exchange items
    """
    endpoint = f"https://eodhistoricaldata.com/api/exchange-symbol-list/{exchange}?api_token={key}&fmt=json"
    print("requesting Data")
    call = requests.get(endpoint).text
    exchange_data = pd.DataFrame(json.loads(call))
    print(exchange_data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()

    root.title("Stock Viewer")
    root.geometry("1024x1024")
    root.configure(bg='#000000')
    def toggle_menu_function():

        def collapse_menu():
            shrink(10, 200)
            toggle_menu.destroy()
            toggle_menu_btn.config(text='☰')
            toggle_menu_btn.config(command=toggle_menu_function)


        toggle_menu = tk.Frame(root,bg='#2c2e30')
        toggle_menu.place(x=0,y=50,height = root.winfo_height(),width=0)


        def expand(count,size):
            if count < 10:
                count += 1
                size += 20
                toggle_menu.place(x=0,y=50,height = root.winfo_height(),width=size)
                toggle_menu.after(10,lambda :expand(count,size))

        def shrink(count,size):
            if count > 0:
                count -= 1
                size -= 20
                toggle_menu.place(x=0,y=50,height=root.winfo_height(),width=size)
                toggle_menu.after(10, lambda:shrink(count, size))


        expand(0,0)
        toggle_menu.grid_columnconfigure(0,weight=1)
        toggle_menu_btn.config(text='✖')
        toggle_menu_btn.config(command=collapse_menu)

        Home_btn = tk.Button(toggle_menu, text="HOME",font=('Bold'),bg='#2c2e30',fg='white',bd=0,activebackground='#2c2e30')
        Home_btn.grid(row=0,column=0)

        Watch_list_btn = tk.Button(toggle_menu, text="Watchlist",font=('Bold'),bg='#2c2e30',fg='white',bd=0,activebackground='#2c2e30')
        Watch_list_btn.grid(row=1,column=0)

        Settings = tk.Button(toggle_menu, text="Settings",font=('Bold'),bg='#2c2e30',fg='white',bd=0,activebackground='#2c2e30')
        Settings.grid(row=2,column=0)

    top_frame = tk.Frame(root,bg='#2c2e30')
    top_frame.pack(side=tk.TOP,fill=tk.X)
    top_frame.pack_propagate(False)
    top_frame.configure(height=50)

    toggle_menu_btn = tk.Button(top_frame,text='☰',font=('Bold'), bg='#2c2e30',bd=0,activebackground='#2c2e30',command=toggle_menu_function)
    toggle_menu_btn.pack(side=tk.LEFT)

    Menu_Label = tk.Label(top_frame,text="MENU",font=('Bold'),bg='#2c2e30',fg='white')
    Menu_Label.pack(side=tk.LEFT)




    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
