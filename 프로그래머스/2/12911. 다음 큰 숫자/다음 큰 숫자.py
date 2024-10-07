def solution(n):
    numOfOne=bin(n).count('1')
    
    while True:
        n+=1
        if numOfOne==bin(n).count('1'):
            return n