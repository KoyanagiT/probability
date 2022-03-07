import correlation
import xlrd

#1次回帰直線
def RegressionReturner1(data1,data2,disp,disp2,disp3,x):
    result = correlation.rReturner2(d,d2,disp)
    a = result[0]/result[2][1]
    b = result[3][0] - a*result[2][0]
    if disp2!=0:
        print("a : {0}".format(a))
        print("b : {0}".format(b))
        if(b<0):
            print("回帰直線 : {0}X{1}".format(round(a,4),round(b,4)))
        else:
            print("回帰直線 : {0}X+{1}".format(round(a,4),round(b,4)))
    if disp3!=0:
        print("y : {0}".format(a*x+b))
    return a,b

if __name__ == "__main__":
    d=[]
    d2=[]
    wb = xlrd.open_workbook('sample.xlsx')
    sheet = wb.sheet_by_name('Sheet1')
    d = sheet.col_values(0)
    d2 = sheet.col_values(1)
    x = 0.64
    RegressionReturner1(d,d2,1,1,1,x)
