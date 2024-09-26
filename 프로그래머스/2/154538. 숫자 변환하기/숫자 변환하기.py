from collections import deque

def solution(x, y, n):
    queue=deque([(x, 0)])
    visited=set([x])
    chk=0
    
    if x==y:
        return 0
    
    while queue:
        v, cnt=queue.popleft()
        if chk!=cnt and v>y:
            return -1        
        
        for num in [v+n, v*2, v*3]:
            if num==y:
                return cnt+1
            if num in visited:
                continue
            else:
                queue.append((num, cnt+1))
                visited.add(num)
        chk=cnt
    
    return -1