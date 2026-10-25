def solution(n, costs):
    
    # 가중치 오름차순 정렬
    costs.sort(key=lambda x : x[2])
    
    # 부모 리스트
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] == x:
            return x
        
        parent[x] = find(parent[x])
        return find(parent[x])
    
    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        
        if parent_a == parent_b:
            return False
        
        parent[parent_a] = parent_b
        return True
    
    answer = 0
    cnt = 0
    
    for a, b, w in costs:
        
        if union(a, b):
            answer += w
            cnt += 1
        
        if cnt == n - 1:
            break
    
    return answer