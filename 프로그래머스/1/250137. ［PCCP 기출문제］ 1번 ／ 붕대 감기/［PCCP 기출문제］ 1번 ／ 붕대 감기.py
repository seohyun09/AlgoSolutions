def solution(bandage, health, attacks):
    time=0
    continuity=0
    maxHealth=health
    lastAttack=attacks[-1][0]
    attackIdx=0
    
    while time<=lastAttack:
        if time==attacks[attackIdx][0]:
            health-=attacks[attackIdx][1]
            attackIdx+=1
            continuity=0
            if health<=0:
                return -1
            time+=1
            continue
        
        health+=bandage[1]
        continuity+=1
        if continuity==bandage[0]:
            health+=bandage[2]
            continuity=0
        if health>maxHealth:
            health=maxHealth
        print(health)
        time+=1
        
    return health