function solution(n) {
    let cnt=0;
    
    if (n==1 || n==2) 
        return 1;
    
    const arr = Array(n).fill(1).map((n, idx)=>n+idx);
    let start=0;
    let end=1;
    let total=arr[start]+arr[end];
    
    while (start<=Math.floor(n/2)) {
        if (total<n) {
            end+=1;
            total+=arr[end];
        } else if (total>n) {
            total-=arr[start];
            start+=1;
        } else if (total==n) {
            cnt+=1;
            total-=arr[start];
            start+=1;
        }
    }
    
    return cnt+1;
}