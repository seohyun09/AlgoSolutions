from collections import deque

def solution(n, edge):
    graph = {}
    answer = {}
    
    for i in range(n):
        graph[i + 1] = []
    
    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    
    visited = [False] * (n + 1)
    
    que = deque()
    que.append((1, 0))
    visited[1] = True
    
    while que:
        node, cnt = que.popleft()
        if cnt not in answer:
            answer[cnt] = []
        answer[cnt].append(node)
        
        for i in range(len(graph[node])):
            val = graph[node][i]
            if not visited[val]:
                visited[val] = True
                que.append((val, cnt + 1))
    
    max_key = max(answer.keys())
    return len(answer[max_key])