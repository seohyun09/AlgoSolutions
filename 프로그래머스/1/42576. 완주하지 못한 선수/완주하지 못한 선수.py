def solution(participant, completion):
    hash_map={}
    
    for person in participant:
        if person in hash_map:
            hash_map[person]+=1
        else:
            hash_map[person]=1
    for complete in completion:
        hash_map[complete]-=1
    
    for key in hash_map:
        if hash_map[key]==1:
            return key
        