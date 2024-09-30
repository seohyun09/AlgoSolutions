def solution(weights):
    cnt=0
    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
            if weights[i]==weights[j]:
                cnt+=1
                continue
            elif weights[i]*2==weights[j] or weights[i]==weights[j]*2:
                cnt+=1
                continue
            elif weights[i]%3==0 or weights[j]%3==0:
                if weights[i]*2==weights[j]*3 or weights[i]*4==weights[j]*3:
                    cnt+=1
                    continue
                if weights[i]*3==weights[j]*2 or weights[i]*3==weights[j]*4:
                    cnt+=1
                    continue
    return cnt