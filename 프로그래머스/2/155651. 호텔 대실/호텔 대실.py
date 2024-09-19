import heapq

def solution(book_time):
    
    def converseToMin(time):
        h, m=time.split(":")
        return int(h)*60+int(m)
    
    # book_time을 모두 분으로 바꾼다
    i=0
    for start, end in book_time:
        book_time[i]=[converseToMin(start), converseToMin(end)+10]
        i+=1
    
    # book_time을 입장 시간 순서로 정렬한다
    book_time.sort(key=lambda x:x[0])
    
    # 우선순위 큐를 만든다
    priority_queue=[]
    
    # book_time을 순회
    numOfRoom=0
    for i in range(len(book_time)):
        if priority_queue:
            if book_time[i][0]>=priority_queue[0][0]:
                heapq.heappop(priority_queue)
                heapq.heappush(priority_queue, (book_time[i][1], book_time[i][0]))
            else:
                numOfRoom+=1
                heapq.heappush(priority_queue, (book_time[i][1], book_time[i][0]))
        else:
            numOfRoom+=1
            heapq.heappush(priority_queue, (book_time[i][1], book_time[i][0]))
    
    return numOfRoom
    
    