t = int(input())

for tc in range(t):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]

    # 3개 연속인지 확인
    def validate_three(col):
        max_cnt = cnt = 1

        for i in range(1, d):
            if film[i][col] == film[i-1][col]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1

        max_cnt = max(max_cnt, cnt)

        if max_cnt >= k:
            return True
        return False

    # 성능검사 통과 여부
    def validate():
        for j in range(w):
            if not validate_three(j):
                break
        else:
            return True

        return False

    answer = d

    def dfs(idx, cnt):
        global answer

        # 가지치기
        if cnt >= answer:
            return

        if validate():
            answer = min(answer, cnt)
            return

        for row in range(idx, d):

            original = film[row][:]

            film[row] = [0] * w
            dfs(row + 1, cnt + 1)

            film[row] = [1] * w
            dfs(row + 1, cnt + 1)

            # 원상 복귀
            film[row] = original

    if validate():
        print(f"#{tc + 1} 0")
    else:
        dfs(0, 0)
        print(f"#{tc + 1} {answer}")



# 얕은 복사 : 겉만 복사, 내부는 공유
# 깊은 복사 : 안쪽까지 새롭게 복사
