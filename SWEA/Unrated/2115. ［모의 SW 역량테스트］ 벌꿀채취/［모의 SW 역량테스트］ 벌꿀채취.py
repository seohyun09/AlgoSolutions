t = int(input())

for tc in range(t):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    total_arr = [[0] * (n-m+1) for _ in range(n)]

    def validate(arr):
        if sum(arr) <= c:
            total = 0
            for i in range(m):
                total += arr[i] ** 2
            return total

        max_sum = 0

        def subset(idx, total, square_sum):
            nonlocal max_sum

            if total > c:
                return

            if idx == m:
                max_sum = max(max_sum, square_sum)
                return

            # 선택
            subset(idx + 1, total + arr[idx], square_sum + arr[idx] ** 2)

            # 선택 안하는 경우
            subset(idx + 1, total, square_sum)

        subset(0, 0, 0)

        return max_sum

    for row in range(n):
        for col in range(n-m+1):
            total_arr[row][col] = validate(arr[row][col:col+m])

    answer = 0

    for r1 in range(n):
        for c1 in range(n - m + 1):
            for r2 in range(n):
                for c2 in range(n - m + 1):
                    if r1 == r2 and abs(c1 - c2) < m:
                        continue
                    answer = max(answer, total_arr[r1][c1] + total_arr[r2][c2])

    print(f"#{tc + 1} {answer}")