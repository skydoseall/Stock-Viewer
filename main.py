# This is a sample Python script.

import tkinter as tk

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()

    root.title("Stock Viewer")
    root.geometry("1024x1024")

    def toggle_menu_function():

        def collapse_menu():
            toggle_menu.destroy()
            toggle_menu_btn.config(text='☰')
            toggle_menu_btn.config(command=toggle_menu_function)

        toggle_menu = tk.Frame(root,bg='#2c2e30')
        toggle_menu.place(x=0,y=50,height = root.winfo_height(),width=200)
        toggle_menu_btn.config(text='✖')
        toggle_menu_btn.config(command=collapse_menu)

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
