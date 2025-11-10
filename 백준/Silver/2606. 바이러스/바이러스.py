import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph={i: [] for i in range(1, n+1)}
for _ in range(m):
  a, b=map(int, sys.stdin.readline().split())
  if a not in graph.keys():
    graph[a]=[]
  if b not in graph.keys():
    graph[b]=[]
  graph[a].append(b)
  graph[b].append(a)

cnt=0
visited=[False]*(n+1)
stack=[]
stack.append(1)

while stack:
  node=stack.pop()
  if not visited[node]:
    visited[node]=True
    cnt+=1
  for u in graph[node]:
    if not visited[u]:
      stack.append(u)

print(cnt-1)
