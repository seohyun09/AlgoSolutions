import java.util.*;

class Solution {
    static int[][] DP;
    
    int solution(int[][] land) {
        
        DP = land;
        
        for (int i = 1; i < land.length; i++) {
            
            for (int j = 0; j < 4; j++) {
                int val = 0;
                
                for (int k = 0; k < 4; k++) {
                    if (j == k) continue;
                    val = Math.max(val, DP[i - 1][k]);    
                }
                DP[i][j] += val;
            }
            
        }
        
        int answer = 0;
        
        for (int j = 0; j < 4; j++) {
            answer = Math.max(answer, DP[land.length - 1][j]);    
        }
        
        return answer;
    }
}   