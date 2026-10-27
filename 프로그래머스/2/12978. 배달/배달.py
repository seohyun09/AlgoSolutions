import heapq

def solution(N, road, K):
    
    INF = float('inf')
    
    # 인접 리스트
    graph = [[] for _ in range(N)]
    
    for a, b, c in road:
        graph[a-1].append((c, b-1))
        graph[b-1].append((c, a-1))
        
    visited = [False] * N
    dist = [INF] * N
    
    def dijkstra(start):
        
        pq = []
        heapq.heappush(pq, (0, start))
        dist[start] = 0
        
        while pq:
            w, curr = heapq.heappop(pq)
            
            if visited[curr]:
                continue
            
            visited[curr] = True
            
            for c, nxt in graph[curr]:
                new_dist = dist[curr] + c
                
                if not visited[nxt] and new_dist < dist[nxt]:
                    dist[nxt] = new_dist
                    heapq.heappush(pq, (new_dist, nxt))
        
        answer = 1
        for i in range(1, N):
            if dist[i] <= K:
                answer += 1
        
        return answer
        
    return dijkstra(0)