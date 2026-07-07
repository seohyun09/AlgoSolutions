import java.util.*;

class Solution {
    public int[] solution(String msg) {
        
        HashMap<String, Integer> Map = new HashMap<>();
        int ascii = 65;
        
        for (int i = 1; i <= 26; i++) {
            Map.put(String.valueOf((char) ascii), i);
            ascii++;
        }
        int length = 26;
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        int idx = 0;
        while (idx < msg.length()) {
            int next = idx + 1;
            String w = msg.substring(idx, next);
            String word = msg.substring(idx, next);
            
            // 가장 긴 문자열 w를 찾는다
            while (true) {                
                next += 1;
                if (next > msg.length()) break;
                word = msg.substring(idx, next);
                int val = Map.getOrDefault(word, 0);
                
                if (val != 0) { // 값이 존재 -> 가장 긴 문자열 w가 아님
                    w = word;
                } else {
                    break;
                }
            }
            
            // answer에 사전 w의 값을 추가한다
            answer.add(Map.get(w));
            
            // (w + c)를 사전에 추가한다
            Map.put(word, ++length);
            
            // idx를 w.length()만큼 이동한다
            idx += w.length();
        }
        
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}