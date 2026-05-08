import java.util.*;

class Solution {
    public int solution(int[] topping) {
        
        HashMap<Integer, Integer> left_map = new HashMap<>();
        HashMap<Integer, Integer> right_map = new HashMap<>();
        
        left_map.put(topping[0], left_map.getOrDefault(topping[0], 0) + 1);
        
        for (int i = 1; i < topping.length; i++) {
            int num = topping[i];
            right_map.put(num, right_map.getOrDefault(num, 0) + 1);
        }
        
        int idx = 1;
        int answer = 0;
        
        while (idx < topping.length - 1) {
            int num = topping[idx];
            
            left_map.put(num, left_map.getOrDefault(num, 0) + 1);
            if (right_map.get(num) == 1) {
                right_map.remove(num);
            } else {
                right_map.put(num, right_map.getOrDefault(num, 0) - 1);
            }
            
            if (left_map.size() == right_map.size()) answer++;
            idx++;
        }
        
        return answer;
    }
}