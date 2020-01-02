# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:20:32 2019

@author: GaonkarN
"""
import pandas as pd
import xlrd

wb = xlrd.open_workbook('jff.xlsx')
print(wb.sheet_names())
sheet = wb.sheet_by_index(0)

data = pd.read_excel(r'jff.xlsx')
df = pd.DataFrame(data, columns=['a', 1])
print(df)
