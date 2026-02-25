def solution(N, number):
    dp = [set() for _ in range(9)]
    
    dp[2].add(N * N)
    dp[2].add(N * 2)
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 * num2)
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num2 - num1)
                    
                    if num1 != 0:
                        dp[i].add(num2 // num1)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
    
        if number in dp[i]:
            return i
    
    return -1