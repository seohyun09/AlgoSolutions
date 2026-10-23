import heapq

def solution(n, roads, sources, destination):
    
    INF = float('inf')
    
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
        
    def dijkstra(start):
        
        visited = [False] * (n + 1)
        dist = [INF] * (n + 1)
        dist[0] = 0
        
        pq = []
        heapq.heappush(pq, (0, start))
        dist[start] = 0
        
        while pq:
            w, curr = heapq.heappop(pq)
            
            visited[curr] = True
            
            for nxt in graph[curr]:
                if visited[nxt]:
                    continue
                    
                new_dist = dist[curr] + 1
                
                if new_dist < dist[nxt]:
                    dist[nxt] = new_dist
                    heapq.heappush(pq, (new_dist, nxt))
                    
        return dist
    
    dist = dijkstra(destination)
    
    answer = []
    
    for node in sources:
        if dist[node] != INF:
            answer.append(dist[node])
        else:
            answer.append(-1)
        
    return answer
            