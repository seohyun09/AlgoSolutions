from heapq import heappush, heappop

t = int(input())

for tc in range(t):
    # n: 한 변에 있는 셀의 개수, m: 격리 시간, k: 미생물 군집 개수
    n, m, k = map(int, input().split())

    hash_map = {}
    for i in range(k):
        ni, nj, num, d = map(int, input().split())
        if (ni, nj) not in hash_map:
            hash_map[(ni, nj)] = []
        heappush(hash_map[(ni, nj)], (num, d))

    # 상(1), 하(2), 좌(3), 우(4)
    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    def change_direction(d):
        if d == 1: return 2
        elif d == 2: return 1
        elif d == 3: return 4
        elif d == 4: return 3

    while m:
        next_map = {}

        for key, val in hash_map.items():
            ni, nj = key[0], key[1]
            num, d = val[0][0], val[0][1]

            ni += di[d]
            nj += dj[d]

            if ni == 0 or ni == n-1 or nj == 0 or nj == n-1:
                num //= 2
                d = change_direction(d)

            # 미생물이 0이 되는 경우
            if num == 0:
                continue

            if (ni, nj) not in next_map:
                next_map[(ni, nj)] = []
            heappush(next_map[(ni, nj)], (num, d))

        for key, val in next_map.items():
            if len(val) >= 2:
                total = 0
                max_num, max_d = 0, 0
                while next_map[key]:
                    num, d = heappop(next_map[key])
                    total += num
                    if num > max_num:
                        max_num = num
                        max_d = d

                next_map[key] = []
                heappush(next_map[key], (total, max_d))
        hash_map = next_map
        m -= 1

    answer = 0

    for key, val in hash_map.items():
        answer += val[0][0]

    print(f"#{tc + 1} {answer}")
