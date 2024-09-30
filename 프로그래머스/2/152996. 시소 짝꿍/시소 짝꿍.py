def solution(weights):
    cnt=0
    hash_map={}
    
    for i in range(len(weights)):
        if weights[i] not in hash_map:
            hash_map[weights[i]]=1
        else:
            hash_map[weights[i]]+=1
    
    numbers=sorted(hash_map.keys())
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            result=numbers[j]/numbers[i]
            if result in [2, 3/2, 4/3]:
                cnt+=hash_map[numbers[i]]*hash_map[numbers[j]]
                
    for num in numbers:
        if hash_map[num]!=1:
            cnt+=(hash_map[num]*(hash_map[num]-1))//2
                
    return cnt
        