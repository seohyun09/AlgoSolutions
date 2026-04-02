from collections import deque

t = int(input())

for tc in range(t):
    # n: 세로 크기, m: 가로 크기, r: 맨홀 세로 위치, c: 맨홀 가로 위치, l: 탈출 소요시간
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    tunnel_type = {
        1: [0, 1, 2, 3],    # 상, 하, 좌, 우
        2: [0, 1],          # 상, 하
        3: [2, 3],          # 좌, 우
        4: [0, 3],          # 상, 우
        5: [1, 3],          # 하, 우
        6: [1, 2],          # 하, 좌
        7: [0, 2]           # 상, 좌
    }

    que = deque()
    que.append((r, c, 1))
    visited[r][c] = True

    def validate(i, j, prev_i, prev_j):
        pos = tunnel_type[arr[i][j]]

        for k in pos:
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
            if ni == prev_i and nj == prev_j:
                return True
        return False


    while que:
        i, j, cnt = que.popleft()

        pos = tunnel_type[arr[i][j]]

        for k in pos:
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if not visited[ni][nj] and cnt < l:

                if arr[ni][nj] and validate(ni, nj, i, j):
                    visited[ni][nj] = True
                    que.append((ni, nj, cnt + 1))

    answer = 0

    for i in range(n):
        answer += sum(visited[i])

    print(f"#{tc + 1} {answer}")