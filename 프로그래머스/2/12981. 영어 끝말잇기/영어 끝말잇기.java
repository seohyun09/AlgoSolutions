import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int length = words.length;
        HashSet<String> set = new HashSet<>();
        
        String prev = "";
        
        for (int i = 0; i < length; i += n) {
            for (int j = 0; j < n; j++) {
                String word = words[i + j];
                
                if (prev.length() > 0 && prev.charAt(prev.length() - 1) 
                    != word.charAt(0)) {
                    return new int[] {j + 1, (i+j) / n + 1};
                }
                
                if (set.contains(word)) {
                    return new int[] {j + 1, (i+j) / n + 1};
                }
                set.add(word);
                
                prev = word;
            }
        }
        
        return new int[] {0, 0};
    }
}