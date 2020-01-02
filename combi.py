# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:20:32 2019

@author: GaonkarN
"""
import numpy as np


def main():
    list1 = ["I", "you"]
    list2 = ["Play", "Love"]
    list3 = ["Hockey", "Football", "Cricket"]
    print("Original Lists:")
    print("list 1")
    print(list1)
    print("List 2")
    print(list2)
    print("List 3")
    print(list3, "\n\n\n")
    new_array = np.array(np.meshgrid(list1, list2, list3)).T.reshape(-1, 3)
    print("all combination of above lists as follows :")
    for row in new_array:
        s1 = " ".join(map(str, row))
        print(s1)


main()
