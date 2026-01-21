t = int(input())

for i in range(t):
  h, w = map(int, input().split())
  
  arr = []
  for j in range(h):
    h_input = input()
    row = []
    for k in range(w):
      if h_input[k] == '#':
        row.append(1)
      else:
        row.append(0)
    
    arr.append(row)
  
  cnt = 0
  for j in range(h):
    if sum(arr[j]) == w:
      cnt += 1
  
  for j in range(w):
    total = 0
    for k in range(h):
      if arr[k][j] == 1:
        total += 1
    
    if total == h:
      cnt += 1
  
  if cnt == h+w:
    cnt -= max(h, w)
  print(cnt)
