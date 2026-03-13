t = int(input())

for tc in range(t):
    a, b, c = map(int, input().split())
    cnt = 0

    if b >= c:
        if c - 1 < 1:
            print(f"#{tc + 1} -1")
            continue
        cnt += (b - c + 1)
        b = c - 1

    if a >= b:
        if b - 1 < 1:
            print(f"#{tc + 1} -1")
        cnt += (a - b + 1)
        a = b - 1

    print(f"#{tc + 1} {cnt}")