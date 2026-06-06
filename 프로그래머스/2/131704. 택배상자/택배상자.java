import java.util.*;

class Solution {
    public int solution(int[] order) {
        
        Stack<Integer> stack = new Stack<>();
        
        int n = order.length;
        Queue<Integer> que = new LinkedList<>();
        
        for (int i = 1; i <= n; i++) {
            que.add(i);
        }
        
        int idx = 0;
        int answer = 0;
        
        while (idx < n) {
            
            int target = order[idx];
            
            if (!que.isEmpty()) {
                int val = que.peek();
                
                if (val == target) {
                    que.poll();
                    answer++;
                } else if (target < val) {
                    if (!stack.isEmpty() && stack.peek() == target) {
                        stack.pop();
                        answer++;
                    } else {
                        break;
                    }
                } else if (val < target) {
                    while (!que.isEmpty()) {
                        int num = que.poll();
                        
                        if (num == target) {
                            answer++;
                            break;
                        } else {
                            stack.push(num);
                        }
                    }
                }
            } else {
                if (!stack.isEmpty() && stack.peek() == target) {
                    stack.pop();
                    answer++;
                } else {
                    break;
                }
            }
            
            idx++;
        }
        
        return answer;
        
    }
}