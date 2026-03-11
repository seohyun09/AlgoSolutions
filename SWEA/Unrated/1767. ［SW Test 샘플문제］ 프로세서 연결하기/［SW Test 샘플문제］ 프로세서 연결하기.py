t = int(input())

for tc in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 가장자리가 아닌 코어들 저장
    cores = []

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1: continue
            if board[i][j] == 1:
                cores.append([i, j])

    max_core = 0
    min_wire = 10000

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    # idx : 현재 처리 중인 코어 번호 (cores 배열 중에서)
    # connected : 지금까지 연결한 코어 개수
    # wire_length : 지금까지 설치한 전선의 총 길이
    def dfs(idx, connected, wire_length):
        global max_core, min_wire, di, dj

        # 종료 조건 : idx가 cores의 길이(개수)와 같아지는 경우
        # 최대 길이 갱신
        # 최소 전선 개수 갱신
        if idx == len(cores):
            if connected > max_core:
                max_core = connected
                min_wire = wire_length
            elif connected == max_core:
                min_wire = min(min_wire, wire_length)
            return

        # (x, y) 선언
        x = cores[idx][0]
        y = cores[idx][1]

        # 4방향 연결 유무 기본 : False
        direction_connected = False

        # 4방향 탐색
        for k in range(4):
            length = 0  # 전선 설치 가능한 경우 길이
            flag = True  # 전선 설치 가능 유무 판단

            ni, nj = x, y

            # 전선 설치 가능 유무 판단
            while True:
                ni += di[k]
                nj += dj[k]

                if ni < 0 or ni >= n or nj < 0 or nj >= n: break

                if board[ni][nj] != 0:
                    flag = False
                    break

            # 전선 설치 가능하면, 전선 표시
            if flag:
                direction_connected = True
                ni, nj = x, y

                while True:
                    ni += di[k]
                    nj += dj[k]

                    if ni < 0 or ni >= n or nj < 0 or nj >= n: break

                    board[ni][nj] = 2
                    length += 1

                # 탐색
                dfs(idx + 1, connected + 1, wire_length + length)

                # 백트래킹으로 전선 제거
                ni, nj = x, y
                while True:
                    ni += di[k]
                    nj += dj[k]

                    if ni < 0 or ni >= n or nj < 0 or nj >= n: break

                    board[ni][nj] = 0

        dfs(idx + 1, connected, wire_length)


    dfs(0, 0, 0)

    print(f"#{tc + 1} {min_wire}")
