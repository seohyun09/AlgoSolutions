from collections import deque

def solution(queue1, queue2):
    
    que1 = deque()
    que2 = deque() 
    N = len(queue1)
    
    for i in range(N):
        que1.append(queue1[i])
        que2.append(queue2[i])
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    target = (sum1 + sum2) // 2
    answer = 0
    
    while True:
        
        if answer > N * 4:
            answer = -1
            break
        
        if sum1 == target:
            break
        
        elif sum1 > target:
            val = que1.popleft()
            sum1 -= val
            sum2 += val
            que2.append(val)
    
        else:
            val = que2.popleft()
            sum2 -= val
            sum1 += val
            que1.append(val)
        
        answer += 1    
    
    return answer
    