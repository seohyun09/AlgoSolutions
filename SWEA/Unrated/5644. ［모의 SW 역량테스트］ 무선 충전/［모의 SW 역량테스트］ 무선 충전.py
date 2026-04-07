t = int(input())

for tc in range(t):
    # m: 총 이동시간, a: BC의 개수
    m, a = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))

    # 무선 충전 정보 저장
    bc_arr = []

    for i in range(a):
        # (x, y): 좌표, c: 충전 범위, p: 처리량
        x, y, c, p = map(int, input().split())
        bc_arr.append((x-1, y-1, c, p))

    x1, y1 = 0, 0
    x2, y2 = 9, 9

    # 이동X(0), 상(1), 우(2), 하(3), 좌(4)
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    a_arr = [0] * m
    b_arr = [0] * m

    def validate_charge(x1, y1, x2, y2):
        a_bc, b_bc = [], []

        # 충전기 순회
        for i in range(a):
            bc_x, bc_y, bc_c, bc_p = bc_arr[i]

            if abs(x1 - bc_x) + abs(y1 - bc_y) <= bc_c:
                a_bc.append(i)
            if abs(x2 - bc_x) + abs(y2 - bc_y) <= bc_c:
                b_bc.append(i)

        max_val = 0

        if len(a_bc) > 0 and len(b_bc) > 0:
            for i in range(len(a_bc)):
                for j in range(len(b_bc)):
                    a1, b1 = a_bc[i], b_bc[j]
                    if a1 == b1:
                        max_val = max(max_val, bc_arr[a1][3])
                    else:
                        max_val = max(max_val, bc_arr[a1][3] + bc_arr[b1][3])
        elif len(a_bc) > 0:
            for i in range(len(a_bc)):
                max_val = max(max_val, bc_arr[a_bc[i]][3])
        elif len(b_bc) > 0:
            for i in range(len(b_bc)):
                max_val = max(max_val, bc_arr[b_bc[i]][3])

        return max_val

    answer = [0] * (m + 1)
    idx = 0

    answer[idx] = validate_charge(x1, y1, x2, y2)

    while idx < m:
        a_dir = move_a[idx]
        b_dir = move_b[idx]

        x1 += dy[a_dir]
        y1 += dx[a_dir]

        x2 += dy[b_dir]
        y2 += dx[b_dir]

        answer[idx + 1] = validate_charge(x1, y1, x2, y2)

        idx += 1

    print(f"#{tc + 1} {sum(answer)}")