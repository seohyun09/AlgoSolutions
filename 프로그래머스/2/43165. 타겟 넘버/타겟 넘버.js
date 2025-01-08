function solution(numbers, target) {
    let length=numbers.length;
    let result=[];
    
    function dfs(depth, node) {
        if (depth===length) {
            result.push(node);
            return
        }
        dfs(depth+1, node+numbers[depth]);
        dfs(depth+1, node-numbers[depth]);
    }
    
    dfs(0, 0);
    
    let cnt=0;
    for (let i=0; i<result.length; i++) {
        if (result[i]===target) cnt+=1;
    }
    
    return cnt;
}
