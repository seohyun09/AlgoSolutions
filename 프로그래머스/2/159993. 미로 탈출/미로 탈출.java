import java.util.*;

class Solution {
    
    static int row_size = 0;
    static int col_size = 0;
    
    // 상(0), 하(1), 좌(2), 우(3)
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};
    
    static char[][] maze;
    
    public int solution(String[] maps) {
        
        row_size = maps.length;
        col_size = maps[0].length();
        
        maze = new char[row_size][col_size];
        int si = 0;
        int sj = 0;
        
        for (int i = 0; i < row_size; i++) {
            for (int j = 0; j < col_size; j++) {
                maze[i][j] = maps[i].charAt(j);
                
                // 시작점 저장
                if (maze[i][j] == 'S') {
                    si = i;
                    sj = j;
                }
            }
        }
        
        // 레버 위치로 이동
        boolean[][] visited = new boolean[row_size][col_size];
        int[] levor = bfs(si, sj, 'L', visited);
        
        if (levor[0] == -1 && levor[1] == -1) {
            return -1;
        }
        
        // 출구로 이동
        visited = new boolean[row_size][col_size];
        int[] arrive = bfs(levor[0], levor[1], 'E', visited);
        
        if (arrive[0] == -1 && arrive[1] == -1) {
            return -1;
        }
        
        return levor[2] + arrive[2];
    }
    
    private int[] bfs(int i, int j, char target, boolean[][] visited) {
        
        Deque<int[]> que = new ArrayDeque<>();
        que.add(new int[] {i, j, 0});
        visited[i][j] = true;
        
        while (!que.isEmpty()) {
            
            int[] curr = que.poll();
            int cnt = curr[2];
            
            if (maze[curr[0]][curr[1]] == target) {
                return new int[] {curr[0], curr[1], cnt};
            }
            
            for (int k = 0; k < 4; k++) {
                int ni = curr[0] + di[k];
                int nj = curr[1] + dj[k];
                
                if (ni < 0 || ni >= row_size || nj < 0 || nj >= col_size) {
                    continue;
                }
                
                if (maze[ni][nj] != 'X' && !visited[ni][nj]) {
                    visited[ni][nj] = true;
                    que.add(new int[] {ni, nj, cnt + 1});
                }
            }
            
        }
        return new int[] {-1, -1, 0};
    }
}