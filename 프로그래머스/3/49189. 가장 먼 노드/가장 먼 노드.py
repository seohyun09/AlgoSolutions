from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for i in range(len(edge)):
        s, e = edge[i]
        graph[s].append(e)
        graph[e].append(s)
        
    que = deque()
    que.append((1, 0))
    visited[1] = True
    
    dist = [[] for _ in range(n + 1)]
    
    while que:
        curr, w = que.popleft()
        
        dist[w].append(curr)
    
        for nxt in graph[curr]:
            if visited[nxt]:
                continue
                
            que.append((nxt, w + 1))
            visited[nxt] = True
    
    for i in range(n, 0, -1):
        if len(dist[i]):
            return len(dist[i])
    