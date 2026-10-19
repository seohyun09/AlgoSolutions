def solution(n, results):
    
    # 인접 행렬
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(len(results)):
        win = results[i][0]
        lose = results[i][1]
        
        # 이겼을 때: 1, 졌을 때: -1
        matrix[win-1][lose-1] = 1
        matrix[lose-1][win-1] = -1
        
    # 플로이드-워셜 알고리즘 수행
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] == 1 and matrix[k][j] == 1:
                    matrix[i][j] = 1
                    matrix[j][i] = -1
    
    # 순위 아는 선수 확인
    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            elif matrix[i][j] != 0:
                cnt += 1
        
        if cnt == n-1:
            answer += 1
            
    return answer