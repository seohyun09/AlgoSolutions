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
            int maxNum = 0;
            for (int j = 0; j < 10; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (maxNum < num) maxNum = num;
            }
            sb.append("#").append(i + 1).append(" ")
                    .append(maxNum).append("\n");
        }
        System.out.println(sb);
    }
}