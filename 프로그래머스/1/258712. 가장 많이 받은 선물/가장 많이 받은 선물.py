def solution(friends, gifts):
    friends_numbering={}
    gift_record = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_score={}
    next_gift_record = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    
    # friends 목록 숫자로 넘버링
    for i in range(len(friends)):
        friends_numbering[friends[i]]=i
    
    # 선물 기록 gift_record에 저장
    for i in range(len(gifts)):
        give, receive=gifts[i].split(' ')
        gift_record[friends_numbering[give]][friends_numbering[receive]]+=1

    # 선물 지수 gift_score 업데이트
    for i in range(len(friends)):
        gift_score[i]=sum(gift_record[i])
    for i in range(len(friends)):
        count=0
        for j in range(len(friends)):
            count+=gift_record[j][i]
        gift_score[i]-=count
    
    # 다음달 선물 예측 next_gift_record
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if gift_record[i][j]>gift_record[j][i]:
                next_gift_record[j][i]=1
            elif gift_record[i][j]<gift_record[j][i]:
                next_gift_record[i][j]=1
            elif (gift_record[i][j]==0 and gift_record[i][j]==0) or gift_record[i][j]==gift_record[i][j]:
                if gift_score[i]<gift_score[j]:
                    next_gift_record[i][j]=1
                elif gift_score[i]>gift_score[j]:
                    next_gift_record[j][i]=1
                elif gift_score[i]==gift_score[j]:
                    continue
    
    total_gift=[]
    for i in range(len(friends)):
        count=0
        for j in range(len(friends)):
            count+=next_gift_record[j][i]
        total_gift.append(count)
        
    return max(total_gift)
            
            
        
        
        