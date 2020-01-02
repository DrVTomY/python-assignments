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
        if flag != 1:
            break;
        else:
                choice = str(input("w=UP s=DOWN d=RIGHT a=LEFT  "))
                steps = int(input("how many steps u want to move : "))
                if choice == 'w':
                    xaxis += steps
                elif choice == 's':
                    xaxis -= steps
                elif choice == 'd':
                    yaxis += steps
                elif choice == 'a':
                    yaxis -= steps
                else:
                    print("Invalid selection")

    reqsteps = abs(xaxis) + abs(yaxis)
    print("total Number of steps Required to reach origin is : ", reqsteps)


main()