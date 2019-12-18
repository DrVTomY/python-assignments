# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:46:32 2019

@author: GaonkarN
"""
from accounttransaction import Bank_Account


def main():
    acc_flag = int(input("to create Bank account press 1 : "))
    if acc_flag == 1 :
        name = str(input("Enter Ur Name : "))
        s = Bank_Account(name)
        flag = 1
        while flag == 1:
            choice = str(input("Press D to Deposit & W to Withdraw & any to show Balance : "))
            if choice == "D":
                amt_d = int(input("Enter The Amount to be Deposited : "))
                s.deposit(amt_d)
            elif choice == "W":
                amt_wd = int(input("Enter The Amount to be Withdrawn : "))
                s.withdraw(amt_wd)
            else:
                s.display()

            flag = int(input("press 1 to continue more transaction : "))
    else:
        print("Invalid selection")


main()

