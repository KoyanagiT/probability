import math as m

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
    data = [1,3,5,4,2,3,10,1,4,6,7,2]
    EVS = EVSReturner(data)
    print(EVS[1])
