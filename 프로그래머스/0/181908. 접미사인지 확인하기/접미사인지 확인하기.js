function solution(my_string, is_suffix) {
    var answer = 0;
    
    for (let i=0; i<my_string.length; i++) {
        if (is_suffix==my_string.substring(i, my_string.length))
            return 1
    }
    return 0    
}