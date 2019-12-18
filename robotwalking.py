# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:40:10 2019

@author: GaonkarN
"""


def main():
    xaxis = 0
    yaxis = 0
    flag = 1

    while flag == 1:
        flag = int(input(" Press 1 for movement "))
        choice = int(input("1=UP 2=DOWN 3=RIGHT 4=LEFT  "))
        steps = int(input("how many steps u want to move : "))
        if choice == 1:
            xaxis += steps
        elif choice == 2:
            xaxis -= steps
        elif choice == 3:
            yaxis += steps
        elif choice == 4:
            yaxis -= steps
        else:
            print("Invalid selection")

    reqsteps = abs(xaxis) + abs(yaxis)
    print("total Number of steps Required to reach origin is : ", reqsteps)


main()

