from collections import deque

def solution(n, roads, sources, destination):
    INF = float('inf')
    
    # 인접행렬
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        start = road[0]
        end = road[1]
        
        graph[start].append(end)
        graph[end].append(start)
    
    def bfs(start):
                
        distance = [INF] * (n + 1)
        distance[0] = 0
        distance[start] = 0
        
        que = deque()
        que.append(start)
        visited = [False] * (n + 1)
        
        while que:
            
            current = que.popleft()
            
            if visited[current]:
                continue
            
            visited[current] = True
            
            for neighbor in graph[current]:
                distance[neighbor] = min(distance[neighbor], distance[current] + 1)
                que.append(neighbor)
        
        return distance
            
    answer = []
    
    distance = bfs(destination)
    
    for node in sources:
        val = distance[node]
        if val == float('inf'):
            answer.append(-1)
        else:
            answer.append(distance[node])    
        
    return answer
    