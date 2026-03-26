# 최소 신장 트리(MST) : 최소 비용의 간선으로 구성됨
# 구현 알고리즘 : Kruskal
    # - 가중치가 최소인 간선부터 선택
    # - 사이클이 생기면 패스
    # 노드 n개의 MST의 간선 개수는 n-1

# Union-Find 알고리즘 : 여러 노드가 존재할 때, 두 노드가 같은 그래프(집합)에 속하는지 판별(find)하고,
# 서로 다른 집합을 하나로 합치는(Union) 상호 배타적 집합 알고리즘
# 구현
    # - 루트 노드의 값이 같으면 순환 O
    # - 루트 노드의 값이 다르면 순환 X


# 다리 만들기 2
# 알고리즘 : BFS/DFS, 그래프, MST, 구현
# 구현 :
    # 1. arr를 순회하며 각 섬을 index를 변환한다
    # 2. 각 섬에서 이을 수 있는 다리를 계산한다(다리 길이: 가중치)
    # 3. --> 그래프로 구현
    # 4. 최소 신장 트리(Kruskal 알고리즘 이용)로 다리의 최소 값 계산

from collections import deque

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# bfs로 섬 탐색하면 인덱스 변환
def bfs(i, j, idx, arr):
    que = deque()
    que.append((i, j))
    arr[i][j] = idx

    while que:
        si, sj = que.popleft()

        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if arr[ni][nj] == 1:
                arr[ni][nj] = idx
                que.append((ni, nj))

    return

# 다리 놓는 함수
def get_edges():
    edges = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:

                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    # 다리 길이
                    length = 0

                    while True:

                        # 범위 밖인 경우
                        if ni < 0 or ni >= n or nj < 0 or nj >= m:
                            break

                        # 바다인 경우
                        if arr[ni][nj] == 0:
                            length += 1

                        # 섬의 가장자리가 아닌 경우
                        elif arr[ni][nj] == arr[i][j]:
                            break

                        # 다른 섬을 만났을 경우
                        else:
                            # 다리 길이가 2 이상인 경우
                            if length >= 2:
                                start = arr[i][j]
                                end = arr[ni][nj]
                                edges.append((length, start, end))
                            break

                        ni += di[k]
                        nj += dj[k]

    return edges


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 주어진 arr의 섬을 인덱스로 변환
# 섬 인덱스 2부터 시작
idx = 2
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j, idx, arr)
            idx += 1

# 섬의 개수
numOfIsland = idx - 2

# 다리 놓기
edges = get_edges()

# 길이가 긴 다리부터 정렬
edges = sorted(edges, key=lambda x: x[0])

# 최소 신장 트리 구현 (Kruskal 알고리즘)
parent = [i for i in range(idx)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    # 사이클 발생
    if rootX == rootY:
        return False

    parent[rootY] = rootX
    return True

numOfBridge = 0
total = 0

for length, x, y in edges:
    if union(x, y):
        numOfBridge += 1
        total += length

if numOfBridge == numOfIsland - 1:
    print(total)
else:
    print(-1)

