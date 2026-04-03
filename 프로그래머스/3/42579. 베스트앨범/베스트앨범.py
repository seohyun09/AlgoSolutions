import heapq

def solution(genres, plays):
    play_map = {}   # 장르별 노래 재생 횟수
    genre_map = {}  # 장르별 노래 횟수와 인덱스
    
    for i in range(len(genres)):
        if genres[i] not in play_map:
            play_map[genres[i]] = 0
            genre_map[genres[i]] = []
        play_map[genres[i]] += plays[i]
        heapq.heappush(genre_map[genres[i]], (-plays[i], i))
        
    
    play_sort = sorted(play_map.items(), key=lambda x: -x[1])
    
    result = []
    for key, _ in play_sort:
        time = 0
        
        while genre_map[key] and time < 2:
            play, idx = heapq.heappop(genre_map[key])
            result.append(idx)
            time += 1
    
    return result