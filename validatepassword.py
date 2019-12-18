# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:13:23 2019

@author: GaonkarN
"""
from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        root.title("Password_Valdation")

        self.label_password = Label(self, text="please insert Password to validate")
        self.entry_password = Entry(self, show="*")
        self.label_password.grid(row=1, sticky=E)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):

        password = self.entry_password.get()

        while True:
            if 5 < len(password) > 13:
                flag = -1
                break
            elif not re.search("[a-z]", password):
                flag = -1
                break
            elif not re.search("[A-Z]", password):
                flag = -1
                break
            elif not re.search("[0-9]", password):
                flag = -1
                break
            elif not re.search("[#@$]", password):
                flag = -1
                break

            else:
                flag = 0
                tm.showinfo("password info", "valid password")
                break

        if flag == -1:
            tm.showerror("password info", "Invalid  password")


root = Tk()
lf = LoginFrame(root)
root.mainloop()
