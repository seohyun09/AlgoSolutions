t = int(input())

for i in range(t):
  x = int(input())

  if x == 1:
    answer = "0"  
  elif x%2 == 0:
    answer = "8" * (x//2)
  else:
    answer = "4" + "8" * (x//2)
  
  print(answer)
