function solution(elements) {
    const set = new Set();
    const length = elements.length;
    
    function cal_sum(idx, l) {
        let total = 0;
        
        for (let i = 0; i < l; i++) {
            let index = (idx + i) % length;
            total += elements[index];
        }
        set.add(total);
        return;
    }
    
    for (let i = 0; i < elements.length; i++) {
        for (let j = 0; j < elements.length; j++) {
            cal_sum(i, j);
        }
    }
    
    return set.size;
}