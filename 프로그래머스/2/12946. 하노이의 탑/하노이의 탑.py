def solution(n):
    answer=[]
    
    def hanoi(start, target, middle, n):
        if n==1:
            answer.append([start, target])
        else:
            hanoi(start, middle, target, n-1)
            hanoi(start, target, middle, 1)
            hanoi(middle, target, start, n-1)
            
    hanoi(1,3,2,n)
    
    return answer