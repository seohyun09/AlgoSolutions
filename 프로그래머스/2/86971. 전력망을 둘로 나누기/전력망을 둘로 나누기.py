from collections import deque

def solution(n, wires):
    
    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    def bfs():
        que = deque()
        que.append(1)
        
        visited = [False] * (n + 1)
        visited[1] = True
        
        cnt = 0
        
        while que:
            curr = que.popleft()
            cnt += 1
            
            visited[curr] = True
            
            for nxt in graph[curr]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
        
        return cnt
    
    answer = n
    
    for s, e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        
        result = bfs()
        
        graph[s].append(e)
        graph[e].append(s)
    
        answer = min(answer, abs(result * 2 - n))
    
    return answer