def solution(n, computers):
    stack=[]
    n=len(computers)
    visited=[False]*n
    
    stack.append(0)
    
    graph={}
    for i in range(n):
        if i not in graph.keys():
            graph[i]=[]
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                graph[i].append(j)
    
    def dfs(stack, visited):
        while stack:
            num=stack.pop()
            visited[num]=True
            
            for node in graph[num]:
                if not visited[node]:
                    stack.append(node)
                    
    numOfNetwork=0
    while sum(visited)!=n:
        for k in range(len(visited)):
            stack.append(k)
            if not visited[k]:
                numOfNetwork+=1
                dfs(stack, visited)
    
    return numOfNetwork
        
        