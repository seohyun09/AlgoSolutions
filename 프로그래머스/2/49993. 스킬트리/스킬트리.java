import java.util.*;
    
class Solution {
    static String SKILL;
    static Set<Character> SET;
    
    public int solution(String skill, String[] skill_trees) {
        
        SET = new HashSet<>();
        SKILL = skill;
        
        for (char c : skill.toCharArray()) {
            SET.add(c);
        }
        
        int cnt = 0;
        
        for (int i = 0; i < skill_trees.length; i++) {
            if (validate(skill_trees[i])) {
                cnt++;
            }
        }
        
        return cnt;
    }
    
    static boolean validate(String word) {
        int idx = 0;
        Set<Character> set = new HashSet<>(SET);
        
        for (int i = 0; i < word.length(); i++) {
            
            if (set.isEmpty()) return true;
            char c = SKILL.charAt(idx);
            
            // 집합에 없으면 다음 문자 탐색
            if (!set.contains(word.charAt(i))) {
                continue;
            
            // 집합에 있으면
            } else {
                
                // SKILL의 문자와 일치
                if (c == word.charAt(i)) {
                    idx++;
                    set.remove(c);
                    
                // SKILL 문자와 일치하지 않는 경우
                } else {
                    return false;
                }
            }
        }
        
        return true;
    }
}