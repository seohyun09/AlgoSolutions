import java.util.*;

class Solution {
    private char[][] BOARD;
    private char[][] NEW;
    
    private int[] di = {0, 1, 1};
    private int[] dj = {1, 0, 1};
    
    public int solution(int m, int n, String[] board) {
        
        BOARD = new char[m][n];
        
        // 2차원 배열에 저장
        for (int i = 0; i < m; i++) {
            
            String line = board[i];
            
            for (int j = 0; j < n; j++) {
                BOARD[i][j] = line.charAt(j);
            }
        }
        
        boolean flag = false;
        
        while (true) {
            
            NEW = new char[m][n];
            
            for (int i = 0; i < m; i++) {
                NEW[i] = BOARD[i].clone();
            }
            
            // 4개 붙어 있는 경우 확인
            // validate로 검증 후, 새 보드에 저장
            for (int i = 0; i < m - 1; i++) {
                for (int j = 0; j < n - 1; j++) {
                    
                    if (BOARD[i][j] == '-') {
                        continue;    
                    }
                    
                    if (validate(i, j, BOARD[i][j])) {
                    
                        NEW[i][j] = '-';
                        for (int k = 0; k < 3; k++) {
                            int ni = i + di[k];
                            int nj = j + dj[k];
                            NEW[ni][nj] = '-';
                        }
                        flag = true;
                    }
                }
            }
            
            if (!flag) {
                break;
            }

            // 새 보드 기본 보드에 복사
            for (int i = 0; i < m; i++) {
                BOARD[i] = NEW[i].clone();
            }

            // 빈 공간 채우기
            for (int col = 0; col < n; col++) {
                int idx = m - 1;
                for (int i = m - 1; i > -1; i--) {
                    if (BOARD[i][col] != '-') {
                        char temp = BOARD[i][col];
                        BOARD[i][col] = BOARD[idx][col];
                        BOARD[idx][col] = temp;

                        idx--;
                    }
                }
            }
            
            flag = false;
            
            // 결과물
            // for (int i = 0; i < m; i++) {
            //     System.out.println(Arrays.toString(BOARD[i]));
            // }
            // System.out.println();
        }
        
        int answer = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (BOARD[i][j] == '-') answer++;
            }
        }
        
        return answer;        
        
    }
    private boolean validate(int si, int sj, char c) {
        
        for (int k = 0; k < 3; k++) {
            int ni = si + di[k];
            int nj = sj + dj[k];
            
            if (BOARD[ni][nj] != c) return false;
        }
        
        return true;
    }
}