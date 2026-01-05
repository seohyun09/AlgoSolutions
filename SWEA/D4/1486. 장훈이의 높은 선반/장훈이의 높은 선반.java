import java.io.*;
import java.util.*;

class Solution {
    static int answer;
    static int b;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            sb.append("#").append(i + 1).append(" ");
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            answer = Integer.MAX_VALUE;

            st = new StringTokenizer(br.readLine());
            int[] tall = new int[n];
            int total = 0;
            for (int j = 0; j < n; j++) {
                tall[j] = Integer.parseInt(st.nextToken());
                total += tall[j];
            }
            back_tracking(0, 0, tall);
            sb.append(answer).append("\n");
        }
        System.out.println(sb);
    }
    private static void back_tracking (int idx, int sum, int[] tall) {
        if (sum >= b) {
            answer = Math.min(answer, sum - b);
            return;
        }
        if (idx == tall.length) return;

        back_tracking(idx + 1, sum + tall[idx], tall);
        back_tracking(idx + 1, sum, tall);
    }
}