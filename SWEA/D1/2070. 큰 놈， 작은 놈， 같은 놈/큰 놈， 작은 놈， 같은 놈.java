import java.io.*;
import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b= Integer.parseInt(st.nextToken());

            sb.append("#").append(i + 1).append(" ");
            if (a < b) {
                sb.append("<").append("\n");
            } else if (a == b) {
                sb.append("=").append("\n");
            } else if (a > b) {
                sb.append(">").append("\n");
            }
        }
        System.out.println(sb);
    }
}