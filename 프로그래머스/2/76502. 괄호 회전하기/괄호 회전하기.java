import java.util.*;

class Solution {
    static Map<Character, Integer> map = Map.of(
        '[', 1,
        ']', 1,
        '(', 2,
        ')', 2,
        '{', 3,
        '}', 3
    );
    
    public int solution(String s) {
        int answer = 0;
        
        for (int i = 0; i < s.length(); i++) {
            
            char front = s.charAt(0);
            s = s.substring(1) + front;            
            
            if (validate(s)) {
                answer++;
            }
        }
        
        return answer;
        
    }
    private boolean validate(String s) {
        
        Stack<Character> stack = new Stack<>();
        
        int idx = 0;
        
        while (idx < s.length()) {
            char op = s.charAt(idx);
            
            if (op == '(' || op == '[' || op == '{') {
                stack.push(op);
            } else {
                if (stack.isEmpty()) return false;
                
                char pop_op = stack.pop();
                
                if (map.get(pop_op) != map.get(op)) return false;
                
            }
            
            idx++;
        }
        
        if (!stack.isEmpty()) return false;
        return true;
    }
}