import heapq

def solution(n, costs):
    
    # 인접 리스트
    graph = [[] for _ in range(n)]
    
    for a, b, w in costs:
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    visited = [False] * n
    
    answer = 0
    cnt = 0
    
    pq = []
    heapq.heappush(pq, (0, 0))
    
    while pq:
        w, curr = heapq.heappop(pq)
        
        if visited[curr]:
            continue
        
        visited[curr] = True
        answer += w
        cnt += 1
        
        for nxt_w, nxt in graph[curr]:
            if not visited[nxt]:
                heapq.heappush(pq, (nxt_w, nxt))
    
    return answer