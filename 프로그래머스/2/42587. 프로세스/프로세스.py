from collections import deque

def solution(priorities, location):
    q=list(deque())
    result=[]
    
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    
    while q:
        arr=q.pop(0)
        priority=arr[0]
        num=arr[1]
        
        if any(priority<item[0] for item in q):
            q.append([priority, num])
        else:
            result.append(num)
    
    for i in range(len(result)):
        if result[i]==location:
            return i+1
        
        