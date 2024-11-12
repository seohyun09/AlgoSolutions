t=int(input())
cnt=0

for _ in range(t):
    cnt+=1
    
    n=int(input())
    s=input()
    
    if s[:len(s)//2]==s[len(s)//2:]:
        print(f'#{cnt} Yes')
    else:
        print(f'#{cnt} No')