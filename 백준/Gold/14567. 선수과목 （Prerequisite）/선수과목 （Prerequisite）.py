# 위상정렬
# 1. DAG (Directed Acyclic Graph : 사이클은 없지만 방향이 있는 그래프이어야 한다.
# 2. 구현 : 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과이다.

from collections import deque

# n : 과목 수 (노드 개수)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

que = deque()

# 진입차수가 0인 노드
for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append((i, 1))

# 결과 저장할 배열
result = [0] * (n + 1)

# 위상 정렬
while que:
    curr, cnt = que.popleft()
    result[curr] = cnt

    for node in graph[curr]:
        indegree[node] -= 1
        if indegree[node] == 0:
            que.append((node, cnt + 1))

print(*result[1:])

