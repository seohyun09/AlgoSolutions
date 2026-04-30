import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int answer = 0;
    static int[][] grid;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        grid = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // search row
        for (int i = 0; i < n; i++) {
            search_row(i, 1, m, 1, grid[i][0]);
        }

        // search column
        for (int j = 0; j < n; j++) {
            search_col(1, j, m, 1, grid[0][j]);
        }

        System.out.print(answer);
    }

    static void search_row(int row, int col, int m, int cnt, int prev) {
        // end condition
        if (col == n) {
            if (cnt >= m) answer++;
            return;
        }

        // pruning
        if (cnt >= m) {
            answer++;
            return;
        }

        if (prev == grid[row][col]) {
            search_row(row, col + 1, m, cnt + 1, grid[row][col]);
        } else {
            search_row(row, col + 1, m, 1, grid[row][col]);
        }
    }

    static void search_col(int row, int col, int m, int cnt, int prev) {
        // end condition
        if (row == n) {
            if (cnt >= m) answer++;
            return;
        }

        // pruning
        if (cnt >= m) {
            answer++;
            return;
        }

        if (prev == grid[row][col]) {
            search_col(row + 1, col, m, cnt + 1, grid[row][col]);
        } else {
            search_col(row + 1, col, m, 1, grid[row][col]);
        }

    }
}