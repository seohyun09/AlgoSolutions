function solution(s) {
    var jadenCase=s.split(" ");
    
    
    
    let n=jadenCase.map((x)=>(x.charAt(0).toUpperCase() + x.slice(1).toLowerCase()));
    
   
    
    return n.join(' ');
}