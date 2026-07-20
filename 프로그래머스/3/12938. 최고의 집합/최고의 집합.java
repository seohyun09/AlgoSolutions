import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        int idx = 0;
        
        while (s > 0 && n > 0) {
            if (s % n == 0) {
                int val = s / n;
                
                for (int i = idx; i < answer.length; i++) {
                    answer[i] = val;
                }
                idx = answer.length;
                break;

            } else {
                int val = s / n + 1;
                answer[idx] = val;
                s -= val;
                n--;
                idx++;
            }
        }
        
        Arrays.sort(answer);
        
        if (idx < answer.length) {
            return new int[] {-1};
        }
        
        return answer;
    }
}