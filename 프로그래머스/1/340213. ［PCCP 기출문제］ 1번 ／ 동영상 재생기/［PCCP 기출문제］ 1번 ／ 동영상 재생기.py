def timeToSec(time):
    m,s=time.split(":")
    return int(m)*60+int(s)

def solution(video_len, pos, op_start, op_end, commands):
    current_time=timeToSec(pos)
    for i in range(len(commands)):
        if timeToSec(op_start) <= current_time <= timeToSec(op_end):
            current_time=timeToSec(op_end)
            
        if commands[i]=="next":
            current_time+=10
        elif commands[i]=="prev":
            current_time-=10
        
        if current_time<0:
            current_time=0
        elif timeToSec(op_start) <= current_time <= timeToSec(op_end):
            current_time=timeToSec(op_end)
        elif current_time>timeToSec(video_len):
            current_time=timeToSec(video_len)
    
    m=current_time//60
    s=current_time%60
    return "{:02d}:{:02d}".format(m, s)