t = int(input())

for tc in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        x, y, d, k = map(int, input().split())
        arr.append([2 * x, 2 * y, d, k])

    # 상(0), 하(1), 좌(2), 우(3)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    answer = 0

    while arr:
        hash_map = {}

        for x, y, d, k in arr:

            nx = x + dx[d]
            ny = y + dy[d]

            if nx < -2000 or nx >= 2000 or ny < -2000 or ny >= 2000:
                continue

            if (nx, ny) not in hash_map:
                hash_map[(nx, ny)] = []
            hash_map[(nx, ny)].append([d, k])
        
        next_arr = []
        
        for key, val in hash_map.items():
            if len(val) >= 2:
                for d, power in val:
                    answer += power

            else:
                d, power = val[0]
                next_arr.append([key[0], key[1], d, power])
        
        arr = next_arr
        
    print(f"#{tc + 1} {answer}")