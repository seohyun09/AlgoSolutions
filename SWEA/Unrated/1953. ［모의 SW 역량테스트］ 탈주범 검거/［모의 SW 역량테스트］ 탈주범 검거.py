from collections import deque

t = int(input())

for tc in range(t):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    tunnel_map = {
        1: [1, 1, 1, 1],
        2: [1, 1, 0, 0],
        3: [0, 0, 1, 1],
        4: [1, 0, 0, 1],
        5: [0, 1, 0, 1],
        6: [0, 1, 1, 0],
        7: [1, 0, 1, 0]
    }

    visited = [[False] * m for _ in range(n)]
    cnt = 1
    que = deque()
    que.append((r, c, 0))
    visited[r][c] = True

    while que:
        i, j, time = que.popleft()

        for k in range(4):
            direction = tunnel_map[arr[i][j]]

            if direction[k] == 0:
                continue

            ni = i + di[k]
            nj = j + dj[k]

            # 범위 확인
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if arr[ni][nj] != 0 and not visited[ni][nj]:
                # 이동한 위치가 이전 통로와의 연결 유무 확인
                flag = False
                for d in range(4):
                    direction = tunnel_map[arr[ni][nj]]

                    if direction[d] == 0:
                        continue

                    prev_i = ni + di[d]
                    prev_j = nj + dj[d]

                    if prev_i < 0 or prev_i >= n or prev_j < 0 or prev_j >= m:
                        continue
                    if prev_i == i and prev_j == j:
                        flag = True
                        break

                if flag:
                    visited[ni][nj] = True

                    if time == l - 1:
                        break

                    que.append((ni, nj, time + 1))
                    cnt += 1


    print(f"#{tc + 1} {cnt}")