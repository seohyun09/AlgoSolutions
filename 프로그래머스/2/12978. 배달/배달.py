def solution(N, road, K):
    
    # 인접 리스트
    graph = [[] for _ in range(N)]
    
    for i in range(len(road)):
        s, e, w = road[i]
        graph[s-1].append([e-1, w])
        graph[e-1].append([s-1, w])
        
    INF = float('inf')
    dist = [INF] * N
    dist[0] = 0
    
    # 방문 배열
    visited = [False] * N
    
    for i in range(N):
        
        min_val = INF
        min_node = -1
        
        for j in range(N):
            if not visited[j] and min_val > dist[j]:
                min_val = dist[j]
                min_node = j
                
        if min_node == -1:
            break
        
        visited[min_node] = True
        
        for e, w in graph[min_node]:
            dist[e] = min(dist[e], min_val + w)
    
    answer = 0
    
    for i in range(N):
        if dist[i] <= K:
            answer += 1
    
    return answer  
    