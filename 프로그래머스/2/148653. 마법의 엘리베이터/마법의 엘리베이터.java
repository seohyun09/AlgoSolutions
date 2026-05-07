class Solution {
    static int length;
    
    public int solution(int storey) {
        String num = String.valueOf(storey);
        length = num.length();
        int answer = 0;
        
        return recur(storey, 0, 0, 0);
    }
    private int recur(int num, int depth, int cnt, int prev) {
        
        if (depth > length) {
            return cnt + prev;
        }
        
        num += prev;
        int remaining = num % 10;
        
        // 0 ~ 4 : 내림
        if (remaining < 5) {
            return recur(num / 10, depth + 1, cnt + remaining, 0);
            
        // 5 : 앞자리 수 보고 판단
        } else if (remaining == 5) {
            // 앞자리 수가 5 이상인 경우
            if ((num / 10) % 10 >= 5) {
                return recur(num / 10, depth + 1, cnt + 5, 1);
            }
            return recur(num / 10, depth + 1, cnt + 5, 0);
            
        // 6 ~ 9 : 올림
        } else {
            return recur(num / 10, depth + 1, cnt + (10 - remaining), 1);
        }
        
    }
}