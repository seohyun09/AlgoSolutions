t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(input().strip()) for _ in range(n)]
    q = int(input()) # 조종 횟수

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                si, sj = i, j
                break

    # 상(0), 우(1), 하(2), 좌(3)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    answer = []

    for _ in range(q):
        c, command = input().split()

        ni, nj = si, sj
        curr_d = 0
        result = 0

        for d in command:
            if d == 'A':
                prev_i, prev_j = ni, nj
                ni += di[curr_d]
                nj += dj[curr_d]

                if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 'T':
                    ni, nj = prev_i, prev_j

            elif d == 'R':
                curr_d = (curr_d + 1) % 4
            elif d == 'L':
                curr_d -= 1
                if curr_d < 0:
                    curr_d = 3
        
        if arr[ni][nj] == 'Y':
            result = 1

        answer.append(result)

    print(f"#{tc + 1} {' '.join(map(str, answer))}")