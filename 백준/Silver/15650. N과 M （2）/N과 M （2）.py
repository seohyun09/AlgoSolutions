def dfs(start):
  if len(arr)==m:
    print(*arr)
    return
  for i in range(start, n+1):
    if visited[i]==True:
      continue
    arr.append(i)
    visited[i]=True
    dfs(i+1)
    arr.pop()
    visited[i]=False

n,m=map(int, input().split())
visited=[False]*(n+1)
arr=[]

dfs(1)