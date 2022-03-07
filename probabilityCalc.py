import xlrd
import collections

#確率計算
def ProbabilityCalc1(data1):
    probabilitys = {}
    size = len(data1)
    co = collections.Counter(data1)
    cokeys = co.keys()
    for i in cokeys:
        probabilitys[i] = co[i] / size
    return  probabilitys
  

#条件付確率(多変数無理，わからん)
# P( data2 | data1 )
def ConditionalProbabilityCalc1(data1, data2):
    probabilitys = {}
    ctj = 0
    ctk = 0
    size = len(data1)
    co1 = collections.Counter(data1)
    cokeys1= co1.keys()
    co2 = collections.Counter(data2)
    cokeys2 = co2.keys()
    for j in cokeys1:
        probabilitys[j]={}
        for k in cokeys2:
            for i in range(size):
                if data1[i]==j:
                    ctj+=1
                    if data2[i]==k:
                        ctk+=1
            probabilitys[j][k] = ctk/ctj
            ctk=0
            ctj=0                    
    return  probabilitys


#同時確率(多変数無理，わからん)
def SimultaneousProbabilityCalc(data1,data2):
    P12 = ConditionalProbabilityCalc1(data1, data2)
    P1  = ProbabilityCalc1(data1)
    co1 = collections.Counter(data1)
    cokeys1= co1.keys()
    co2 = collections.Counter(data2)
    cokeys2 = co2.keys()
    probabilitys = {}
    for i in cokeys1:
        probabilitys[i] = {}
        for j in cokeys2:
            probabilitys[i][j] = P12[i][j] * P1[i]            
    return  probabilitys 


if __name__ == "__main__":
    d=[]
    d2=[]
    wb = xlrd.open_workbook('sample.xlsx')
    sheet = wb.sheet_by_name('Sheet1')
    d = sheet.col_values(0)
    d2 = sheet.col_values(1)
    result = SimultaneousProbabilityCalc(d,d2)
    print(result)
