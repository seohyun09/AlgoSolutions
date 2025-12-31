import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringBuilder st = new StringBuilder();
        for (int i = 0; i < n; i++) {
            st.append('#');
        }

        System.out.print(st);
    }
}