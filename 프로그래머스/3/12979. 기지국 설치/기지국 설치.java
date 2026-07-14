class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int prev = 1;
        int unit = w * 2 + 1;
        
        for (int station : stations) {
            int start = station - w <= 0 ? 1 : station - w;
            int end = station + w >= n ? n : station + w;
            
            if (start - prev <= 0) {
                prev = end + 1;
            } else {
                int gap = start - prev;                
                answer += (gap + unit -1) / unit;
                prev = end + 1;
            }
        }
        
        if (prev <= n) {
            int gap = n - prev + 1;
            answer += (gap + unit - 1) / unit;
        }

        return answer;
    }
}
