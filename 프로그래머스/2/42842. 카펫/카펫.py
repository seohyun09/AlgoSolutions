def solution(brown, yellow):
    n,m=1,1
    while True:
        if yellow%n==0:
            m=yellow//n
            
            if n*2+m*2+4==brown:
                return max(n,m)+2, min(n,m)+2
        n+=1
                