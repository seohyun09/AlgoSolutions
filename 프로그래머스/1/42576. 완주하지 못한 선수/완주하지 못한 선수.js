function solution(participant, completion) {
    var hash_map={};
    
    for (person of participant) {
        if (person in hash_map)
            hash_map[person]+=1;
        else
            hash_map[person]=1;
    }
    for (complete of completion) 
        hash_map[complete]-=1;
    
    for (key in hash_map) {
        if (hash_map[key]===1)
            return key;
    }
}