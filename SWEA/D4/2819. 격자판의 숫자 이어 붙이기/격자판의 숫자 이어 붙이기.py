t = int(input())

for tc in range(t):
    arr = [list(input().split()) for _ in range(4)]
    number_set = set()

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def recursive(cnt, i, j, number):
        if cnt == 7:
            number_set.add(number)
            return

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or ni >= 4 or nj < 0 or nj >= 4: continue

            recursive(cnt + 1, ni, nj, number + arr[ni][nj])

    for i in range(4):
        for j in range(4):
            recursive(0, i, j, "")
            
    print(f"#{tc + 1} {len(number_set)}")