class Solution {
    public int solution(int n) {        
        if (n <= 3) return n;
        
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        
        int idx = 4;
        
        while (idx <= n) {
            dp[idx] = ((1 * dp[idx - 1]) + (2 * dp[idx - 2]) - dp[idx - 2]) % 1000000007;
            idx++;
        }
        
        return dp[n];
    }
}