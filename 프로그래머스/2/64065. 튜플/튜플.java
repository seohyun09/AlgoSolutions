import java.util.*;

class Solution {
    public int[] solution(String s) {
        s = s.substring(1, s.length() - 1);
              
        String[] parts = s.split("},");
        ArrayList<int[]> arr = new ArrayList<>();        
        
        for (String part : parts) {
            
            if (part.charAt(part.length() - 1) == '}') {
                part = part.substring(1, part.length() - 1);
            } else {
                part = part.substring(1);
            }
            
            String[] nums = part.split(",");
            int[] numArr = new int[nums.length];
            
            for (int i = 0; i < nums.length; i++) {
                numArr[i] = Integer.parseInt(nums[i]);
            }
            arr.add(numArr);
        }
        
        // 집합 길이에 따라 정렬
        arr.sort(Comparator.comparingInt(a -> a.length));
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int[] num : arr) {
            
            for (int i = 0; i < num.length; i++) {
                if (!list.contains(num[i])) {
                    list.add(num[i]);
                    break;
                }
            }
            
        }
        
        int[] answer = new int[arr.size()];
        int idx = 0;
        
        for (int n : list) {
            answer[idx] = list.get(idx);
            idx++;
        }
        
        return answer;
    }
}