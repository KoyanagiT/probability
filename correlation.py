import EVSRe
import xlrd
import probabilityCalc
import collections
import math
   

#相互情報量
def IReturner(data1,data2):
    Ps = probabilityCalc.SimultaneousProbabilityCalc(data1,data2)
    P1 = probabilityCalc.ProbabilityCalc1(data1)
    P2 = probabilityCalc.ProbabilityCalc1(data2)
    I = 0
    co1 = collections.Counter(data1)
    cokeys1= co1.keys()
    co2 = collections.Counter(data2)
    cokeys2 = co2.keys()
    for i in cokeys1:
        for j in cokeys2:
            if Ps[i][j]/(P1[i]*P2[j]) != 0:
               I+= Ps[i][j]*math.log10(Ps[i][j]/(P1[i]*P2[j]))
            
    return I

            
#相関係数
def rReturner2(data1,data2,disp):
    EVS1 = EVSRe.EVSReturner(data1)
    EVS2 = EVSRe.EVSReturner(data2)
    size = len(data1)
    sam = 0
    for i in range(size):
        sam += (data1[i]-EVS1[0])*(data2[i]-EVS2[0])
    Sxy = sam/size
    r = Sxy/(EVS1[2]*EVS2[2])
    if disp!=0:
        if(abs(r*100) < 1):
            if(r!=0):
                print("ほぼほぼ",end="")
            print("無相関なんですけど")
        elif(r<0):
            if(r<=-0.5):
                print("強い",end="")
            print("負の相関があります")
        elif(r>0):
            if(r>=0.5):
                print("強い",end="")
            print("正の相関があります")            
        print("xの平均 : {0}".format(EVS1[0]))
        print("yの平均 : {0}".format(EVS2[0]))
        print("xの分散 : {0}".format(EVS1[1]))
        print("yの分散 : {0}".format(EVS2[1]))
        print("xの標準偏差 : {0}".format(EVS1[2]))
        print("yの標準偏差 : {0}".format(EVS2[2]))
        print("共分散 : {0}".format(Sxy))
        print("相関係数 : {0}".format(r))
        print("相互情報量 : {0}".format(IReturner(data1,data2)))
    
    return Sxy,r,EVS1,EVS2

if __name__ == "__main__":
    d=[]
    d2=[]
    wb = xlrd.open_workbook('sample.xlsx')
    sheet = wb.sheet_by_name('Sheet1')
    d = sheet.col_values(0)
    d2 = sheet.col_values(1)
    result = rReturner2(d,d2,1)
    
