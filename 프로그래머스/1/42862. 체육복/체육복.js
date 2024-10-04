function solution(n, lost, reserve) {
    
    for (let i=0; i<reserve.length; i++) {
        if (lost.includes(reserve[i])) {
            lost.splice(reserve[i])
            reserve[i]=0
        }        
    }
    
    lost.sort()
    reserve.sort()
    
    for (let i=0; i<reserve.length; i++) {
        if (reserve[i]==0)
            continue
        else if (lost.includes(reserve[i]-1)) {
            lost.splice(reserve[i]-1)
        } else if (lost.includes(reserve[i]+1)) {
            lost.splice(reserve[i]+1)
        }
    
    if (lost.length>0)
        return n-lost.length
    else
        return n
    }
}