def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, visited, computers)
            
    return answer

def dfs(start, visited, computers):
    n = len(computers)
    stack = [start]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            
            neighbor = computers[node]
            for j in range(n):
                if neighbor[j] == 1 and not visited[j]:
                    stack.append(j)
    
    return
    
    