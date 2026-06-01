import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        
        HashMap<String, Integer> map1 = makeMap(str1);
        HashMap<String, Integer> map2 = makeMap(str2);
        
        int intersect = 0;
        int map1Values = 0;
        int map2Values = 0;
        
        for (Map.Entry<String, Integer> entry : map1.entrySet()) {
            String key = entry.getKey();
            int val = entry.getValue();
            
            int map2_val = map2.getOrDefault(key, 0);
            
            if (map2_val != 0) {
                intersect += Math.min(val, map2_val);
            }
        }
        
        if (map1.isEmpty() && map2.isEmpty()) {
            return 65536;
        }
        
        int map1_values = 0;
        int map2_values = 0;
        
        for (int val : map1.values()) {
            map1_values += val;
        }
        for (int val : map2.values()) {
            map2_values += val;
        }
        
        int union = map1_values + map2_values - intersect;
        
        return intersect * 65536 / union;
    }
    
    static HashMap<String, Integer> makeMap(String str) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < str.length() - 1; i++) {
            String parse = str.substring(i, i + 2).toLowerCase();
            
            char c1 = parse.charAt(0);
            char c2 = parse.charAt(1);
            
            if (c1 >= 97 && c1 <= 122 && c2 >= 97 && c2 <= 122) {
                map.put(parse, map.getOrDefault(parse, 0) + 1);
            }
        }
        return map;
    }
    
    
}