t = int(input())

for tc in range(t):
    # n: 셀의 개수, m: 격리 시간, k: 미생물 군집의 개수
    n, m, k = map(int, input().split())
    arr = []

    for _ in range(k):
        # 세로, 가로, 미생물 수, 이동방향
        row, col, num, d = map(int, input().split())
        arr.append([row, col, num, d])

    time = m

    # 상(1), 하(2), 좌(3), 우(4)
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    while time > 0:
        next_arr = []
        hash_map = {}

        for i, j, num, d in arr:
            ni = i + di[d]
            nj = j + dj[d]

            next_num, next_d = num, d

            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue

            # 가장자리 도달
            if ni == 0 or ni == n-1 or nj ==0 or nj == n-1:
                next_num //= 2

                if next_d == 1:
                    next_d = 2
                elif next_d == 2:
                    next_d = 1
                elif next_d == 3:
                    next_d = 4
                else:
                    next_d = 3

            if next_num == 0:
                continue

            if (ni, nj) not in hash_map:
                hash_map[(ni, nj)] = []
            hash_map[(ni, nj)].append((next_num, next_d))

        for key, val in hash_map.items():
            if len(val) >= 2:
                total = 0
                max_num = 0
                max_d = 0
                
                for cnt, d in val:
                    total += cnt
                    if cnt > max_num:
                        max_num = cnt
                        max_d = d
                next_arr.append([key[0], key[1], total, max_d])
                
            else:
                next_arr.append([key[0], key[1], val[0][0], val[0][1]])

        arr = next_arr

        time -= 1

    answer = 0

    # 남은 미생물 수 확인
    for i, j, num, d in arr:
        answer += num

    print(f"#{tc + 1} {answer}")
