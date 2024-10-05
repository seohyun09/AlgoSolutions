def solution(s):
    result=[0, 0]
    
    while True:
        result[1]+=(len(s)-eliminateZero(s))
        s=changeToBinary(eliminateZero(s))
        result[0]+=1
        
        if s=="1":
            return result
    

def eliminateZero(x):
    x=str(x)
    numOfOne=0
    for i in range(len(x)):
        if x[i]=="1":
            numOfOne+=1
    return numOfOne

def changeToBinary(num):
    arr=[]
    while num>0:
        arr.append(num%2)
        num=num//2
    arr.reverse()
    return ''.join(map(str, arr))
    