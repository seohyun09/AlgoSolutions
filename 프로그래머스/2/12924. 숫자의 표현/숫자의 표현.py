def solution(n):
    cnt=0
    
    if n==1 or n==2:
        return 1
    
    arr=list(range(1, n+1))
    start, end=0, 1
    total=arr[start]+arr[end]
    
    while start<=n//2:
        if total<n:
            end+=1
            total+=arr[end]
        elif total>n:
            total-=arr[start]
            start+=1
        elif total==n:
            cnt+=1
            total-=arr[start]
            start+=1
    
    return cnt+1
        