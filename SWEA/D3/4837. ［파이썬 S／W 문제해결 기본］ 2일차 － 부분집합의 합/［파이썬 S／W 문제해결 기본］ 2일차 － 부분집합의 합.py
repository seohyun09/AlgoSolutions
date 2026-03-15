t = int(input())
A = list(range(1, 13))

for tc in range(t):
    # n : 원소 개수
    # k : 원소의 합
    n, k = map(int, input().split())
    cnt = 0

    def recur(selected, start):
        global cnt

        if len(selected) == n:
            if sum(selected) == k:
                cnt += 1
            return

        for i in range(start, 12):
            selected.append(A[i])
            recur(selected, i + 1)
            selected.pop()

    recur([], 0)

    print(f"#{tc + 1} {cnt}")