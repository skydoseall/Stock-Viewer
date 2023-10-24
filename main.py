# This is a sample Python script.

import tkinter as tk
import json
import pandas as pd
import requests
import time
from tkinter import ttk
import sv_ttk
import Get_Data
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()

    sv_ttk.set_theme("dark")
    root.tk.call('source', 'forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')
    root.title("Stock Viewer")
    root.geometry("1024x1024")
    root.configure(bg='#000000')
    def toggle_menu_function():

        root.update_idletasks()
        def collapse_menu():
            shrink(10, 200)
            toggle_menu.destroy()
            toggle_menu_btn.config(text='☰')
            toggle_menu_btn.config(command=toggle_menu_function)


        toggle_menu = tk.Frame(root,bg='#2c2e30')
        toggle_menu.place(x=0,y=50,height = root.winfo_height(),width=0)


        def expand(count,size):
            if count < 20:
                count += 1
                size += 10
                toggle_menu.place(x=0,y=50,height = root.winfo_height(),width=size)
                toggle_menu.after(5,lambda :expand(count,size))

        def shrink(count,size):
            if count > 0:
                count -= 1
                size -= 20
                toggle_menu.place(x=0,y=50,height=root.winfo_height(),width=size)
                toggle_menu.after(10, lambda:shrink(count, size))

        def on_enter(e):
            e.widget['background'] = '#f5f8fc'
            e.widget['fg'] = 'black'

        def on_leave(e):
            e.widget['background'] = '#2c2e30'
            e.widget['fg'] = 'white'


        expand(0,0)
        toggle_menu.grid_columnconfigure(0,weight=1)
        toggle_menu_btn.config(text='✖')
        toggle_menu_btn.config(command=collapse_menu)

        Home_btn = tk.Button(toggle_menu, text="HOME",font=('Bold'),bg='#2c2e30',fg='white',bd=0,activebackground='#2c2e30')
        Home_btn.bind("<Enter>", on_enter)
        Home_btn.bind("<Leave>", on_leave)
        Home_btn.grid(row=0,column=0,sticky="nsew")

        Watch_list_btn = tk.Button(toggle_menu, text="Watchlist",font=('Bold'),bg='#2c2e30',fg='white',bd=0,activebackground='#2c2e30')
        Watch_list_btn.bind("<Enter>", on_enter)
        Watch_list_btn.bind("<Leave>", on_leave)
        Watch_list_btn.grid(row=1,column=0,sticky="nsew")

        Settings = tk.Button(toggle_menu, text="Settings",font=('Bold'),bg='#2c2e30',fg='white',bd=0,activebackground='#2c2e30')
        Settings.bind("<Enter>", on_enter)
        Settings.bind("<Leave>", on_leave)
        Settings.grid(row=2,column=0,sticky="nsew")

    top_frame = tk.Frame(root,bg='#2c2e30')
    top_frame.pack(side=tk.TOP,fill=tk.X)
    top_frame.pack_propagate(False)
    top_frame.configure(height=50)

    toggle_menu_btn = tk.Button(top_frame,text='☰',font=('Bold'), bg='#2c2e30',bd=0,activebackground='#2c2e30',command=toggle_menu_function)
    toggle_menu_btn.pack(side=tk.LEFT)

    Menu_Label = tk.Label(top_frame,text="MENU",font=('Bold'),bg='#2c2e30',fg='white')
    Menu_Label.pack(side=tk.LEFT)

    Tree_Frame = tk.Frame(root)
    Tree_Frame.columnconfigure(0, weight = 1)
    Tree_Frame.rowconfigure(0,weight=1)
    Tree_Frame.pack(fill=tk.BOTH,expand=1)

    Home_treeview = ttk.Treeview(Tree_Frame,selectmode='browse')
    Home_treeview['columns'] = ("Code","Name","Country","Exchange","Currency","Type","Current Price")
    Home_treeview.column("#0",width=0,stretch = "no")
    Home_treeview.column("Code", minwidth=10, width=100)
    Home_treeview.column("Name",minwidth=10, width=100)
    Home_treeview.column("Country",minwidth=10, width=100)
    Home_treeview.column("Exchange",minwidth=10, width=100)
    Home_treeview.column("Currency",minwidth=10, width=100)
    Home_treeview.column("Type",minwidth=10, width=100)
    Home_treeview.column("Current Price",minwidth=10, width=100)

    Home_treeview.heading("Code",text="Code")
    Home_treeview.heading("Name", text="Name")
    Home_treeview.heading("Country", text="Country")
    Home_treeview.heading("Exchange", text="Exchange")
    Home_treeview.heading("Currency", text="Currency")
    Home_treeview.heading("Type", text="Type")
    Home_treeview.heading("Current Price", text="Current Price")

    Home_treeview.columnconfigure(0, weight = 1)
    Home_treeview.rowconfigure(0,weight=1)
    Home_treeview.grid(row=0,column=0,sticky="nswe")

    vsb = ttk.Scrollbar(Tree_Frame, command=Home_treeview.yview)
    vsb.grid(row=0,column=1,sticky="ns")


    search_btn = tk.Button(top_frame,text='⌕',font=('Bold'), bg='#2c2e30',bd=0,activebackground='#2c2e30',command=lambda :(Get_Data.get_specific_data(search_box.get("1.0","end-1c"),Home_treeview)))
    search_box = tk.Text(top_frame,width=30,height=20,wrap='none')
    search_btn.pack(side=tk.RIGHT,pady=10)
    search_box.pack(side=tk.RIGHT,pady=13)

    Get_Data.Get_Curr_Data(Home_treeview)

    root.mainloop()
