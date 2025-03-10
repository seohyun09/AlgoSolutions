def dfs():
  if len(arr)==m:
    print(*arr)
    return
  for i in range(1, n+1):
    if visited[i]:
      continue
    arr.append(i)
    visited[i]=True
    dfs()
    arr.pop()
    visited[i]=False

n,m=map(int, input().split())
visited=[False]*(n+1)
arr=[]

dfs()