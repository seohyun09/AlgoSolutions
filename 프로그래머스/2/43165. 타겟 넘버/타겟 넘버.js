function solution(numbers, target) {
    var arr=[0];
    
    for (let i=0; i<numbers.length; i++) {
        var temp=[];
        for (let j=0; j<arr.length; j++) {
            temp.push(arr[j]+numbers[i]);
            temp.push(arr[j]-numbers[i]);
        }
        arr=temp;
    }
    
    let cnt=0;
    for (let i=0; i<arr.length; i++) {
        if (arr[i]===target) cnt+=1;
    }
    
    return cnt;
}