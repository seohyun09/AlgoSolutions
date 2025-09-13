def solution(k, tangerine):
    hash_map={}
    for i in range(len(tangerine)):
        if tangerine[i] in hash_map.keys():
            hash_map[tangerine[i]]+=1
        else:
            hash_map[tangerine[i]]=1
    
    sorted_hash_map=sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
    
    total=0
    for i in range(len(sorted_hash_map)):
        total+=sorted_hash_map[i][1]
        if total>=k:
            return i+1