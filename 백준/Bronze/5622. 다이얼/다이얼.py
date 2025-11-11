str=input()
dial=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

sum=0

for i in range(len(str)):
    sum+=dial[ord(str[i])-ord('A')]

sum+=len(str)
print(sum)