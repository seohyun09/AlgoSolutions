def solution(k, dungeons):
    
    n = len(dungeons)
    visited = [False] * n
    
    answer = 0
    
    def backtracking(ph, visited, cnt):
        nonlocal answer
        
        answer = max(answer, cnt)
        
        for i in range(n):
            need, use = dungeons[i]
            if not visited[i] and ph >= need:
                visited[i] = True
                backtracking(ph - use, visited, cnt + 1)
                visited[i] = False
        
    backtracking(k, visited, 0)
        
    return answer
    