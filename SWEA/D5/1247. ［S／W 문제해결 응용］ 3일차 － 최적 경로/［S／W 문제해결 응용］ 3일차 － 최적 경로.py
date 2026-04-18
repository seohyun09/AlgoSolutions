t = int(input())

for tc in range(t):
    n = int(input())
    sx, sy, tx, ty, *arr = map(int, input().split())
    visited = [False] * n

    n_arr = []
    for i in range(0, len(arr), 2):
        n_arr.append((arr[i], arr[i + 1]))

    answer = 10000

    def recur(prev_x, prev_y, cnt, dist, visited):
        global answer

        if cnt == n:
            end_distance = abs(prev_x - tx) + abs(prev_y - ty)
            answer = min(answer, dist + end_distance)
            return

        if dist > answer:
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                distance = abs(prev_x - n_arr[i][0]) + abs(prev_y - n_arr[i][1])
                recur(n_arr[i][0], n_arr[i][1], cnt + 1, dist + distance, visited)
                visited[i] = False

    recur(sx, sy, 0, 0, [False] * n)

    print(f"#{tc + 1} {answer}")