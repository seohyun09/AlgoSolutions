import java.io.*;
import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                sb.append(i).append(" ");
            }
        }
        System.out.println(sb);
    }
}