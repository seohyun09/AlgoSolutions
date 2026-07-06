import java.util.*;

class Solution {
    
    public long solution(int n, int[] works) {
                
        PriorityQueue<Integer> PQ = new PriorityQueue<>();
        for (int num : works) {
            PQ.offer(-num);
        }
        
        while (n > 0 && !PQ.isEmpty()) {
            int val = -PQ.poll() - 1;
            
            if (val > 0) {
                PQ.offer(-val);
            }
            
            n--;
        }
    
        long result = 0;
        for (int num : PQ) {
            result += num * num;
        }
        
        return result;
        
    }
}