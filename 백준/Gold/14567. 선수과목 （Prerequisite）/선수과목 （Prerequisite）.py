from collections import deque

n, m = map(int, input().split())
# 진입차수
indegree = [0] * (n + 1)
# 연결된 자식 노드 저장하는 그래프
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

answer = [0] * (n + 1)

que = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append((i, 1))

while que:
    node, cnt = que.popleft()
    answer[node] = cnt

    for neighbor in graph[node]:
        indegree[neighbor] -= 1

        if indegree[neighbor] == 0:
            que.append((neighbor, cnt + 1))


print(*answer[1:])