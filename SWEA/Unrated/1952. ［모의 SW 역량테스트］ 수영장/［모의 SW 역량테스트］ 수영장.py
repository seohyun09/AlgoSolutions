t = int(input())

for tc in range(t):
    one_day, one_month, three_month, one_year = map(int, input().split())
    month_plan = list(map(int, input().split()))

    answer = one_year

    def recursive(month, total):
        global answer

        # 종료조건
        if month > 11:
            answer = min(answer, total)
            return

        # 가지치기
        if total >= answer:
            return

        # 하루씩
        recursive(month + 1, total + month_plan[month] * one_day)

        # 한 달
        if month_plan[month] != 0:
            recursive(month + 1, total + one_month)
            # 세 달
            recursive(month + 3, total + three_month)
        else:
            recursive(month + 1, total)

    recursive(0, 0)

    print(f"#{tc + 1} {answer}")


