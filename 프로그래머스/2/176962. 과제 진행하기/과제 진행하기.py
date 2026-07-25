def solution(plans):
    answer = []
    
    plans.sort(key = lambda x: x[1])
    
    stopped = []
    
    for i in range(len(plans) - 1):
        name = plans[i][0]
        start = timeToMinute(plans[i][1])
        playtime = int(plans[i][2])
        
        next_start = timeToMinute(plans[i + 1][1])
        
        if start + playtime == next_start:
            answer.append(name)
        elif start + playtime < next_start:
            answer.append(name)
            gap = next_start - (start + playtime)
            
            if not stopped:
                continue
            
            # 남은 시간동안 멈춘 과목 수행
            while stopped:
                stop_name, left_time = stopped.pop()
                
                if left_time == gap:
                    answer.append(stop_name)
                elif left_time > gap:
                    left_time -= gap
                    stopped.append([stop_name, left_time])
                    break
                else:
                    answer.append(stop_name)
                    gap -= left_time
            
        elif start + playtime > next_start:  
            left_time = (start + playtime) - next_start
            stopped.append([name, left_time])
    
    answer.append(plans[-1][0])
    while stopped:
        answer.append(stopped.pop()[0])
    
    return answer

def timeToMinute(time):
        splited = time.split(":")
        h = int(splited[0])
        m = int(splited[1])
        
        return h * 60 + m