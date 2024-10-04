function solution(n, slicer, num_list) {
    var [a, b, c]=slicer
    if (n==1) {
        return num_list.slice(0,b+1)
    } else if (n==2) {
        return num_list.slice(a,num_list.length)
    } else if (n==3) {
        return num_list.slice(a,b+1)
    } else if (n==4) {
        let arrFour=[]
        for (let i=a; i<b+1; i+=c)
            arrFour.push(num_list[i])
        return arrFour
    }
}