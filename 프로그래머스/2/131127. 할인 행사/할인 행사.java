import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int start = 0;
        int end = 9;
        
        HashMap<String, Integer> hash_map = new HashMap<>();
        
        for (int i = 0; i < 10; i++) {
            hash_map.put(discount[i], hash_map.getOrDefault(discount[i], 0) + 1);
        }
        
        int answer = 0;
        
        while (start <= discount.length - 10) {
            boolean flag = true;
            
            for (int i = 0; i < want.length; i++) {
                if (hash_map.getOrDefault(want[i], 0) != number[i]) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) answer++;
            
            if (start == discount.length - 10) break;
                        
            hash_map.put(discount[start], hash_map.get(discount[start]) - 1);
            
            start++;
            end++;
            
            hash_map.put(discount[end], hash_map.getOrDefault(discount[end], 0) + 1);
            
        }
        
        return answer;
    }
}