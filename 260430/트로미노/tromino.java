import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] grid;
    static int answer;

    static int[][][] shapes = {
        // line shape
        {{0, 0}, {0, 1}, {0, 2}},
        {{0, 0}, {1, 0}, {2, 0}},

        // L shape
        {{0, 0}, {1, 0}, {1, 1}},
        {{0, 0}, {1, 0}, {0, 1}},
        {{0, 0}, {0, 1}, {1, 1}},
        {{0, 0}, {1, 0}, {1, -1}}
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        grid = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int s = 0; s < shapes.length; s++) {
                    validate(i, j, shapes[s]);
                }
            }
        }

        System.out.println(answer);
    }

    static void validate(int i, int j, int[][] arr) {
        int sum = 0;

        for (int k = 0; k < 3; k++) {
            int ni = i + arr[k][0];
            int nj = j + arr[k][1];

            if (ni < 0 || ni >= n || nj < 0 || nj >= m) return;

            sum += grid[ni][nj];
        }

        answer = Math.max(answer, sum);
    }
}