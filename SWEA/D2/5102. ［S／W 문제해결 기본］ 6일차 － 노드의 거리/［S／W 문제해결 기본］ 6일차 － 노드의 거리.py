from collections import deque

t = int(input())

for tc in range(t):
    # 노드 개수, 간선 개수
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 출발 노드, 도착 노드
    s, g = map(int, input().split())

    answer = 0

    visited = [False] * (v + 1)

    que = deque()
    que.append((s, 0))
    visited[s] = True

    while que:
        node, dist = que.popleft()
        
        if node == g:
            answer = dist

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                que.append((neighbor, dist + 1))


    print(f"#{tc + 1} {answer}")