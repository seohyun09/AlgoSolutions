function solution(num_list) {
    a=num_list[num_list.length-1]
    b=num_list[num_list.length-2]
    
    if (a<=b)
        num_list.push(a*2)
    else
        num_list.push(a-b)
    
    return num_list
}