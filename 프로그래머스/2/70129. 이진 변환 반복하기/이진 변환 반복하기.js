function solution(s) {
    let result=[0, 0];
    while (s!=="1") {
        result[1]+=s.length-eliminateZero(s);
        s=changeToBinary(eliminateZero(s));
        result[0]+=1;
    }
    return result;
}


function eliminateZero(x) {
    let count=0;
    for (let i=0; i<x.length; i++) {
        if (x[i]=="1")
            count+=1;
    }
    return count;
}

function changeToBinary(num) {
    let arr=[];
    while (num>0) {
        arr.push(num%2);
        num=Math.floor(num/2);
    }
    return arr.reverse().join('');
}