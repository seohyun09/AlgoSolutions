def solution(s):
    stack=[]
    for i in range(len(s)):
        if stack and stack[-1]==s[i]:
            stack.append(s[i])
            stack.pop()
            stack.pop()
        else:
            stack.append(s[i])
            
    if stack:
        return 0
    else:
        return 1