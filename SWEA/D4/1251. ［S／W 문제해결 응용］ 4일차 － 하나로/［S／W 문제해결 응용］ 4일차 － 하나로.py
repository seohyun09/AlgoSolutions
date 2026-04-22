from heapq import heappush, heappop

t = int(input())

for tc in range(t):
    # n: 섬 개수
    n = int(input())
    # 섬들의 x좌표, y좌표
    x_arr = list(map(int, input().split()))
    y_arr = list(map(int, input().split()))
    # e: 환경 부담 세율
    e = float(input())

    graph = [[] for _ in range(n)]

    # 섬들의 좌표 그래프로 변환
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = x_arr[i], y_arr[i]
            x2, y2 = x_arr[j], y_arr[j]

            weight = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) * e

            graph[i].append((weight, j))
            graph[j].append((weight, i))

    # Prim 알고리즘
    def Prim(start):
        MST = [0] * n

        # 가중치, 정점 선택 개수
        min_w, node_cnt = 0, 0

        heap = []
        heappush(heap, (0, start))

        while node_cnt < n and heap:
            w, node = heappop(heap)

            if MST[node]:
                continue

            MST[node] = 1
            min_w += w
            node_cnt += 1

            for nw, nv in graph[node]:
                heappush(heap, (nw, nv))

        return min_w

    print(f"#{tc + 1} {round(Prim(0))}")