import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        int cnt = 0;
        int a_idx = 0;
        int b_idx = 0;
        
        while (b_idx < B.length) {
            if (A[a_idx] < B[b_idx]) {
                a_idx++; b_idx++;
                cnt++;
            } else {
                b_idx++;
            }
        }
        
        return cnt;
    }
}