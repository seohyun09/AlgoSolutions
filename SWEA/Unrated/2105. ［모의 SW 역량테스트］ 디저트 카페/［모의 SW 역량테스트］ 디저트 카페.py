t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]

    type_map = {0: [3],
                1: [2, 3],
                2: [0, 2],
                3: [0, 1],
                4: [1]}

    answer = -1

    def dfs(i, j, cnt, node_type, node_set, prev, start_i, start_j):
        global answer

        direction = type_map[node_type]
        for k in direction:
            ni = i + di[k]
            nj = j + dj[k]

            if ni == start_i and nj == start_j and node_type >= 3:
                answer = max(answer, cnt)
                return

            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue

            if arr[ni][nj] in node_set:
                continue

            node_set.add(arr[ni][nj])

            if k == prev:
                dfs(ni, nj, cnt + 1, node_type, node_set, k, start_i, start_j)
            else:
                dfs(ni, nj, cnt + 1, node_type + 1, node_set, k, start_i, start_j)

            node_set.remove(arr[ni][nj])


    for si in range(n - 1):
        for sj in range(1, n-1):
            initial_set = set()
            initial_set.add(arr[si][sj])
            dfs(si, sj, 1, 0, initial_set, -1, si, sj)

    print(f"#{tc + 1} {answer}")
