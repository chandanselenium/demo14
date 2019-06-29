import pandas as pd

filepath=r'E:\actitime1\testdata.xlsx'

xl=pd.read_excel(filepath,sheet_name=0)

col=xl[0:1]

print(col)



