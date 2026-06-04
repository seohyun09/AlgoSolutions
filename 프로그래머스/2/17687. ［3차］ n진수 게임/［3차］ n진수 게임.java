class Solution {
    public String solution(int n, int t, int m, int p) {
        
        String answer = "";
        String arr = "";
        
        int num = 0;
        
        while (arr.length() < m * t) {
            arr += Integer.toString(num, n);
            num++;
        }
        
        for (int i = 0; i < t; i++) {
            int pos = (p - 1) + m * i;
            char c = arr.charAt(pos);
            
            if (c >= 97 && c < 123) {
                c = Character.toUpperCase(c);
            }
            
            answer += c;
        }
        
        return answer;
    }
}