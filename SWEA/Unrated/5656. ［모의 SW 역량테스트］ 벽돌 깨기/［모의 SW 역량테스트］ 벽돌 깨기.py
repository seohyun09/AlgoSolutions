import copy

t = int(input())

for tc in range(t):
    # n: 구슬 개수, w: 가로 너비, h: 세로 높이
    n, w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    answer = 10000

    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def bfs(i, j, arr):
        power = arr[i][j]
        arr[i][j] = 0

        for d in range(4):

            ni, nj = i, j
            cnt = 0

            while cnt < power - 1:

                ni += di[d]
                nj += dj[d]

                if ni < 0 or ni >= h or nj < 0 or nj >= w:
                    break

                if arr[ni][nj]:
                    bfs(ni, nj, arr)

                cnt += 1


    def dfs(arr, time):
        global answer

        # 종료조건
        if time == n:
            total = 0
            for i in range(h):
                for j in range(w):
                    if arr[i][j]:
                        total += 1
            answer = min(answer, total)
            return

        for j in range(w):

            for i in range(h):
                if arr[i][j]:
                    copy_arr = copy.deepcopy(arr)
                    bfs(i, j, copy_arr)

                    # 중력 처리
                    for col in range(w):
                        idx = h - 1
                        for row in range(h-1, -1, -1):
                            if copy_arr[row][col]:
                                copy_arr[row][col], copy_arr[idx][col] = copy_arr[idx][col], copy_arr[row][col]
                                idx -= 1

                    dfs(copy_arr, time + 1)
                    break

            else:
                dfs(arr, time + 1)

    dfs(arr, 0)

    print(f"#{tc + 1} {answer}")
