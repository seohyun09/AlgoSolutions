import java.io.*;
import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][n];
            int[][] answer = new int[n][n];

            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < n; k++) {
                    arr[j][k] = Integer.parseInt(st.nextToken());
                }
            }

            sb.append("#").append(i + 1).append("\n");
            String[] nintyDegree = new String[n];
            String[] oneEightyDegree = new String[n];
            String[] twoSeventiyDegree = new String[n];

            // 90도
            for (int j = 0; j < n; j++) {
                String num = "";
                for (int k = n - 1; k > -1; k--) {
                    num += String.valueOf(arr[k][j]);
                }
                nintyDegree[j] = num;
            }

            // 180도
            for (int j = n - 1; j > -1; j--) {
                String num = "";
                for (int k = n - 1; k > -1; k--) {
                    num += String.valueOf(arr[j][k]);
                }
                oneEightyDegree[n - j - 1] = num;
            }

            // 270도
            for (int j = n - 1; j > -1; j--) {
                String num = "";
                for (int k = 0; k < n; k++) {
                    num += String.valueOf(arr[k][j]);
                }
                twoSeventiyDegree[n - j - 1] = num;
            }

            for (int j = 0; j < n; j++) {
                sb.append(nintyDegree[j]).append(" ")
                        .append(oneEightyDegree[j]).append(" ")
                        .append(twoSeventiyDegree[j]).append("\n");
            }
        }
        System.out.println(sb);
    }
}