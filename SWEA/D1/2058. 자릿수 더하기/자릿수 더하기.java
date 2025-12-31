import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String n = br.readLine();

        int answer = 0;

        for (char c : n.toCharArray()) {
            answer += Integer.parseInt(String.valueOf(c));
        }

        System.out.print(answer);
    }
}