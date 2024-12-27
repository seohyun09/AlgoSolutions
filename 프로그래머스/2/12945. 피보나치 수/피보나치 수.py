import sys
sys.setrecursionlimit(10 ** 6)

def solution(n):
    arr=[]
    for i in range(n+1):
        if i==0 or i==1:
            arr.append(i)
        else:
            arr.append((arr[i-2]+arr[i-1])%1234567)
    return arr[n]