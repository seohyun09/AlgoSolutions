def solution(arr):
    arr.sort()
    cmpr=lcm(arr[0], arr[1])
    if len(arr)==2:
        return cmpr
    else:
        for i in range(2, len(arr)):
            cmpr=lcm(cmpr, arr[i])
        return cmpr

def lcm(a,b):
    return (a*b)/gcd(a,b)

def gcd(a,b):
    while (b!=0):
        r=a%b
        a=b
        b=r
    return a