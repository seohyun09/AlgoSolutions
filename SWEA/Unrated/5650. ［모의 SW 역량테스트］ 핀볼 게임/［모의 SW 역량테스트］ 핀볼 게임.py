t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 상(0), 하(1), 좌(2), 우(3)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 블록 부딪히는 방향에 따라 바뀌는 방향
    block_dir = {
        # 각각 상, 하, 좌, 우로 와서 부딪힐 때 바뀌는 방향 인덱스
        1: [1, 3, 0, 2],
        2: [3, 0, 1, 2],
        3: [2, 0, 3, 1],
        4: [1, 2, 3, 0],
        5: [1, 0, 3, 2]
    }

    hole_map = {}

    # 웜홀 위치 저장
    for i in range(n):
        for j in range(n):
            if 6 <= arr[i][j] <= 10:
                if arr[i][j] not in hole_map:
                    hole_map[arr[i][j]] = []
                hole_map[arr[i][j]].append((i, j))

    answer = 0

    def recursive(i, j):
        global answer

        for k in range(4):
            score = 0
            ni, nj = i, j

            while True:
                ni += di[k]
                nj += dj[k]

                # 벽에 부딪힌 경우
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    # 방향 반대로 바뀜. 상(0) <-> 하(1) | 좌(2) <-> 우(3)
                    if k == 0: k = 1
                    elif k == 1: k = 0
                    elif k == 2: k = 3
                    elif k == 3: k = 2

                    score += 1
                    continue

                # 블랙홀을 만나거나 출발 위치로 돌아오는 경우
                if arr[ni][nj] == -1 or (ni == i and nj == j):
                    answer = max(answer, score)
                    break

                # 웜홀에 빠지는 경우
                elif 6 <= arr[ni][nj] <= 10:
                    for x, y in hole_map[arr[ni][nj]]:
                        if x == ni and y == nj:
                            continue
                        else:
                            ni = x
                            nj = y
                            break
                    continue

                # 블록에 부딪히는 경우
                elif 1 <= arr[ni][nj] <= 5:
                    k = block_dir[arr[ni][nj]][k]
                    score += 1

    # 전체 순회하며 모든 경우의 수 확인
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                recursive(i, j)

    print(f"#{tc + 1} {answer}")