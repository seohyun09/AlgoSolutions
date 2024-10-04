def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for num in reserve[:]:
        if num in lost:
            lost.remove(num)
            reserve.remove(num)
    for num in reserve:
        if num-1 in lost:
            lost.remove(num-1)
        elif num+1 in lost:
            lost.remove(num+1)
    if lost:
        return n-len(lost)
    else:
        return n