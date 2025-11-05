import heapq
def solution(genres, plays):
    numOfGenres={}
    plays_map={}
    answer=[]
    for i in range(len(genres)):
        if genres[i] not in numOfGenres.keys():
            numOfGenres[genres[i]]=plays[i]
            plays_map[genres[i]]=[]
        else:
            numOfGenres[genres[i]]+=plays[i]
        heapq.heappush(plays_map[genres[i]], (-plays[i], i))
    
    numOfGenres=dict(sorted(numOfGenres.items(), key=lambda x:x[1], reverse=True))
    
    for genre in numOfGenres:
        num, idx=heapq.heappop(plays_map[genre])
        answer.append(idx)
        if plays_map[genre]:
            num, idx=heapq.heappop(plays_map[genre])
            answer.append(idx)
        
    return answer
    

    