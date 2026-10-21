from collections import deque

def solution(priorities, location):
    
    que = deque()
    for i in range(len(priorities)):
        que.append([i, priorities[i]])
    
    cnt = 0
    
    while que:
        idx, val = que.popleft()
        
        flag = False
        for i in range(len(que)):
            if val < que[i][1]:
                que.append([idx, val])
                flag = True
                break
        
        # 프로세스를 큐에 넣지 않는 경우
        if not flag:
            cnt += 1
            if idx == location:
                return cnt
        