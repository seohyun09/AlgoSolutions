class Solution {
    public String solution(String number, int k) {
        
        return dfs(number, k);
    }
    
    private String dfs(String number, int k) {
        // 종료조건
        if (k == 0) {
            return number;
        }
        
        if (number.length() == k) return "";
        
        int max_val = number.charAt(0) - '0';
        int max_idx = 0;
        
        // k 범위 내 최대값, 최대값 인덱스 저장
        for (int i = 1; i <= k; i++) {
            int digit = number.charAt(i) - '0';
            if (digit > max_val) {
                max_val = digit;
                max_idx = i;
            }
        }

        return number.charAt(max_idx) + dfs(number.substring(max_idx + 1), k - max_idx);
    }
}