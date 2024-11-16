from collections import deque

t=int(input())
cnt=0

for _ in range(t):
    cnt+=1
    n,m=map(int, input().split())
    R_hashmap={}
    W_hashmap={}
    q=deque()
    total=0

    parking=[0 for _ in range(n)]

    for i in range(1, n+1):
        num=int(input())
        R_hashmap[i]=num
    for i in range(1, m+1):
        num=int(input())
        W_hashmap[i]=num
    
    for i in range(2*m):
        car=input()

        if q:
            for i in range(n):
                if parking[i]==0:
                    if q:
                        carIdx=q.popleft()
                        parking[i]=carIdx
                        total+=R_hashmap[i+1]*W_hashmap[carIdx]
                    else:
                        break
        
        if car[0]=='-':
            for i in range(n):
                if parking[i]==int(car[1:]):
                    parking[i]=0
                    break            
        else:
            for i in range(n):
                chk=0
                if parking[i]==0:
                    chk=1
                    parking[i]=int(car)
                    total+=R_hashmap[i+1]*W_hashmap[int(car)]
                    break
            if chk==0:
                q.append(int(car))
        
    print(f'#{cnt} {total}')
                    