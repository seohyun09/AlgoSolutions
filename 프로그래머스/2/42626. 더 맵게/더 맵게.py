import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0
    
    while True:
        num1=heapq.heappop(scoville)
        if len(scoville)==0 and num1<K:
            return -1
        elif len(scoville)==0 and num1>K:
            return cnt
        num2=heapq.heappop(scoville)
        
        if num1<K:
            heapq.heappush(scoville, num1+num2*2)
        else:
            return cnt
        
        cnt+=1