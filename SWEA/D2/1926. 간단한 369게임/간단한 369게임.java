import java.util.*;
import java.io.*;

class Solution
{
	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        
        for (int i = 1; i <= n; i++) {
            String num = String.valueOf(i);
            int flag = 0;
            for (int j = 0; j < num.length(); j++) {
                if (num.charAt(j) == '3' || num.charAt(j) == '6' || num.charAt(j) == '9') {
                    sb.append("-");
                    flag = 1;
                }
            }
            if (flag == 0) sb.append(i);
            sb.append(" ");            
        }
        System.out.print(sb);
	}
}