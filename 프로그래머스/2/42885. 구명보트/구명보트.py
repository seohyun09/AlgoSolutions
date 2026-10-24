def solution(people, limit):
    
    n = len(people)
    visited = [False] * n
    
    people.sort()
    left, right = 0, n - 1
    
    cnt = 0
    
    while left < right:
        
        if people[left] + people[right] <= limit:
            cnt += 1
            left += 1
            right -= 1
        else:
            cnt += 1
            right -= 1
        
        if left == right:
            cnt += 1
            break
    
    
    return cnt