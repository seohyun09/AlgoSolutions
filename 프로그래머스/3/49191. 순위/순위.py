def solution(n, results):
    
    # 인접 행렬
    graph = [[-1] * n for _ in range(n)]
    
    for i in range(len(results)):
        win = results[i][0]
        lose = results[i][1]
        
        # 승리: 1, 패: 0
        graph[win-1][lose-1] = 1
        graph[lose-1][win-1] = 0
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = 0
                elif graph[i][k] == 0 and graph[k][j] == 0:
                    graph[i][j] = 0
                    graph[j][i] = 1
                    
    answer = 0
    
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            elif graph[i][j] != -1:
                cnt += 1
        
        if cnt == n-1:
            answer += 1
            
    return answer