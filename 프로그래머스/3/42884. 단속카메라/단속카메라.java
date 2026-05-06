import java.util.*;

class Solution {
    static int[][] ROUTES;
    static int length;
    
    public int solution(int[][] routes) {
        length = routes.length;
        boolean[] visited = new boolean[length];
        
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));
        ROUTES = routes;
        
        int answer = recursive(1, 1, ROUTES[0][1]);
        
        return answer;
    }
    
    private int recursive(int idx, int cnt, int prev) {
        if (idx == length) {
            return cnt;
        }
        
        if (ROUTES[idx][0] <= prev && prev <= ROUTES[idx][1]) {
            return recursive(idx + 1, cnt, prev);
        }
        
        return recursive(idx + 1, cnt + 1, ROUTES[idx][1]);
        
    }
    
}