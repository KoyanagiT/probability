import math as m
import xlrd

def EVSReturner(data):
    size = len(data)
    sam=0
    for i in range(size):
        sam+=data[i]
    E = sam/size
    sam=0
    for i in range(size):
        sam+=(data[i]-E)**2
    V = sam/size
    S = m.sqrt(V)
    return E,V,S

if __name__ == "__main__":
    d=[]
    d2=[]
    wb = xlrd.open_workbook('sample.xlsx')
    sheet = wb.sheet_by_name('Sheet1')
    d = sheet.col_values(0)
    d2 = sheet.col_values(1)
    EVS1 = EVSReturner(d)
    EVS2 = EVSReturner(d2)
    print("xの平均 : {0}".format(EVS1[0]))
    print("yの平均 : {0}".format(EVS2[0]))
    print("xの分散 : {0}".format(EVS1[1]))
    print("yの分散 : {0}".format(EVS2[1]))
    print("xの標準偏差 : {0}".format(EVS1[2]))
    print("yの標準偏差 : {0}".format(EVS2[2]))
