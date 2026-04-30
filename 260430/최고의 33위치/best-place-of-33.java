import java.util.Scanner;
public class Main {
    static int[][] grid;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        // Please write your code here.

        int answer = 0;

        for (int i = 0; i < n-2; i++) {
            for (int j = 0; j < n-2; j++) {
                answer = Math.max(answer, validate(i, j));        
            }
        }

        System.out.println(answer);
    }
    static int validate(int row, int col) {
        int total = 0;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[row + i][col + j] == 1) total++;
            }
        }
        return total;
    }
}