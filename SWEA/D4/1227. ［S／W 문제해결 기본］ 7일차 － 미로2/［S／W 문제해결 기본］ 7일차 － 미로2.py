for _ in range(10):
    tc = int(input())

    maze = [list(map(int, input())) for _ in range(100)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = []
    stack.append((1, 1))
    visited = [[False] * 100 for _ in range(100)]
    answer = False

    while stack:
        x, y = stack.pop()

        if maze[x][y] == 3:
            answer = True
            break

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 100 and 0 <= ny < 100:
                if not visited[nx][ny] and maze[nx][ny] != 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    print(f"#{tc} {1 if answer else 0}")