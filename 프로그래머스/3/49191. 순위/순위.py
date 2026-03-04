def solution(n, results):
    graph = [[0] * n for _ in range(n)]
    
    for i in range(len(results)):
        winner = results[i][0] - 1
        looser = results[i][1] - 1
        
        graph[winner][looser] = 1
        graph[looser][winner] = -1
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][j] == 1 and graph[j][k] == 1:
                    graph[i][k] = 1
                    graph[k][i] = -1
    
                if graph[i][j] == -1 and graph[j][k] == -1:
                    graph[i][k] = -1
                    graph[k][i] = 1
    
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] !=0 :
                cnt += 1
        if cnt == n-1:
            answer += 1
    
    return answer