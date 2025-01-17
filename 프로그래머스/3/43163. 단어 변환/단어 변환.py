def solution(begin, target, words):
    if target not in words:
        return 0
    
    length=len(words)
    visited=[0 for _ in range(length)]
    depth=0
    target_idx=findTarget(words, target)
    if target_idx==-1:
        return 0
    else:
        visited[target_idx]=1
    
    arr=[]
    arr.append(target)
    
    while arr:
        for i in range(len(arr)):
            if numOfSame(arr[i], begin)==len(arr[i])-1:
                return depth+1
            elif sum(visited)==length:
                return 0

            temp=[]
            for j in range(length):
                if visited[j]==1:
                    continue
                elif numOfSame(arr[i], words[j])==len(arr[i])-1:
                    temp.append(words[j])
                    visited[j]=1
            arr=temp
            depth+=1
    return 0

            
def findTarget(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
def numOfSame(word1, word2):
    cnt=0
    for i in range(len(word1)):
        if word1[i]==word2[i]:
            cnt+=1
    return cnt