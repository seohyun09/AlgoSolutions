import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
  line=sys.stdin.readline().strip()
  arr.append(list(map(int, line)))

def recursive(arr):
  
  flat=sum([sum(row) for row in arr])
  if flat==0:
    return "0"
  if flat==len(arr)*len(arr):
    return "1"
  
  n=len(arr)//2

  left_up=[row[:n] for row in arr[:n]]
  right_up=[row[n:] for row in arr[:n]]
  left_bottom=[row[:n] for row in arr[n:]]
  right_bottom=[row[n:] for row in arr[n:]]

  return ("(" +
    recursive(left_up) +
    recursive(right_up) +
    recursive(left_bottom) +
    recursive(right_bottom) +
  ")")

print(recursive(arr))