def solution(n, costs):

    edges = []

    for s, e, w in costs:
        edges.append([w, s, e])

    edges.sort()

    # 1. 각 노드의 부모 정보를 저장할 parent 배열 생성
    #    - 섬 번호는 0부터 n-1까지 존재
    #    - 처음에는 자기 자신을 부모로 설정
    parent = [i for i in range(n)]

    # 2. find(x) 함수 구현
    #    - x가 속한 집합의 최상위 부모(루트)를 찾는 함수
    #    - parent[x] == x 라면 x를 반환
    #    - 아니라면 parent[x]를 따라가서 최상위 부모를 찾음
    #    - 이때 경로 압축을 적용하면 효율적
    def find(x):
        if parent[x] == x:
            return x
        
        parent[x] = find(parent[x])
        return parent[x]

    # 3. union(a, b) 함수 구현
    #    - find(a), find(b)를 통해 각각의 최상위 부모를 찾음
    #    - 두 부모가 다르면 한쪽 루트를 다른 쪽 루트에 연결
    #    - 이때 부모 배열의 값을 수정해야 함
    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        
        if parent_a != parent_b:
            parent[parent_a] = parent_b
            
        return

    # 4. MST의 총비용을 저장할 변수 초기화
    cost = 0

    # 5. 선택한 간선의 개수를 저장할 변수 초기화
    numOfEdge = 0

    # 6. edges를 순회하면서 가중치, 시작 노드, 끝 노드를 꺼냄
    
        # 7. 시작 노드와 끝 노드의 최상위 부모를 find로 확인

        # 8. 두 노드의 최상위 부모가 서로 다르다면
        #    - 현재 간선을 추가해도 사이클이 발생하지 않음
        #    - union을 이용해 두 집합을 합침
        #    - 현재 간선의 가중치를 총비용에 더함
        #    - 선택한 간선의 개수를 1 증가

        # 9. 선택한 간선이 n-1개가 되었다면
        #    - MST 완성
        #    - 반복문 종료
    
    for w, s, e in edges:
        if find(s) != find(e):
            union(s, e)
            cost += w
            numOfEdge += 1
            
        if numOfEdge == n-1:
            break

    # 10. MST의 총비용 반환

    return cost
