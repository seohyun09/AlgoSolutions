def solution(numbers):
    stack=[]
    result=[]
    
    for i in range(len(numbers)-1, -1, -1):
        if len(stack)==0:
            stack.append(numbers[i])
            result.append(-1)
            continue
        while len(stack)!=0 and numbers[i]>=stack[-1]:
            stack.pop()
        if len(stack)!=0:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(numbers[i])
            
    result.reverse()
    return result