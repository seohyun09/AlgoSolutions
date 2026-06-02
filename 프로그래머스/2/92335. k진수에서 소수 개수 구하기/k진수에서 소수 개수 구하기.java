import java.util.*;

class Solution {
    public int solution(int n, int k) {
        
        // k 진법으로 변환
        String num = Integer.toString(n, k);
        // 0을 기준으로 분리
        String[] arr = num.split("0");
        
        int answer = 0;
        
        ArrayList<Integer> numArr = new ArrayList<>();
        
        for (String item : arr) {
            if (item.length() == 0) continue;
            
            long val = Long.parseLong(item);
            
            if (validatePrime(val)) answer++;
        }
        
        return answer;
    }
    
    static boolean validatePrime(long num) {
        if (num < 2) return false;
        
        for (long i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}