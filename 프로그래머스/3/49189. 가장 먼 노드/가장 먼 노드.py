import heapq

def solution(n, edge):
    
    INF = float('inf')
    
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    
    for i in range(len(edge)):
        s, e = edge[i]
        graph[s].append(e)
        graph[e].append(s)
        
    
    def dijkstra(node):
        
        visited = [False] * (n + 1)
        dist = [INF] * (n + 1)
        dist[0] = 0
        dist[node] = 0
        
        pq = []
        heapq.heappush(pq, (0, node))
        visited[node] = True
        
        while pq:
            weight, current = heapq.heappop(pq)
            
            visited[current] = True
            
            for nxt in graph[current]:
                new_dist = weight + 1
                
                if not visited[nxt] and new_dist < dist[nxt]:
                    dist[nxt] = new_dist
                    pq.append((new_dist, nxt))
              
        max_val = max(dist)
        cnt = 0
        for i in range(1, n + 1):
            if dist[i] == max_val:
                cnt += 1
        
        return cnt
    
    return dijkstra(1)
            