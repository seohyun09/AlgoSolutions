def solution(sequence, k):
    start, end=0,0
    current_sum=sequence[0]
    answer=[]

    while end<len(sequence):
        if current_sum<k:
            if end<len(sequence)-1:
                end+=1
                current_sum+=sequence[end]
            else:
                break
        elif current_sum>k:
            current_sum-=sequence[start]
            start+=1
        else:
            answer.append([start, end])
            if start==end:
                if end<len(sequence)-1:
                    end+=1
                    current_sum+=sequence[end]
                else:

                    break
            else:
                current_sum-=sequence[start]
                start+=1

    answer.sort(key=lambda x:(x[1]-x[0], x[0]))

    return answer[0]