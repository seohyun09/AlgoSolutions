class Solution {
    // 상(0), 하(1), 좌(2), 우(3)
    static int[] di = {1, -1, 0, 0};
    static int[] dj = {0, 0, -1, 1};
    
    public int solution(String dirs) {
        
        int answer = 0;
        int curr_i = 5;
        int curr_j = 5;
        
        int[][][] moveDir = new int[11][11][4];
        
        for (char c : dirs.toCharArray()) {
            int dir = setDir(c);
            
            int ni = curr_i + di[dir];
            int nj = curr_j + dj[dir];
            
            // 범위를 벗어나는 경우
            if (ni < 0 || ni >= 11 || nj < 0 || nj >= 11) continue;
            
            // 방문하지 않는 경우
            if (moveDir[ni][nj][changeDir(dir)] == 0) {
                moveDir[curr_i][curr_j][dir] = 1;
                moveDir[ni][nj][changeDir(dir)] = 1;
                answer++;
            }
            
            curr_i = ni;
            curr_j = nj;
        }
        
        return answer;
    }
    static int setDir(char c) {
        if (c == 'U') return 0;
        else if (c == 'D') return 1;
        else if (c == 'R') return 3;
        else if (c == 'L') return 2;
        return -1;
    }
    
    static int changeDir(int d) {
        if (d == 0) return 1;
        else if (d == 1) return 0;
        else if (d == 2) return 3;
        else if (d == 3) return 2;
        return -1;
    }
}