import java.io.*;
import java.util.*;

public class Solution {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			sb.append("#").append(tc + 1).append("\n");
			
			int n = Integer.parseInt(br.readLine());
			Set<String> name_set = new HashSet<>();
			
			// 이름 중복 제거
			for (int i = 0; i < n; i++) {
				String name = br.readLine();
				name_set.add(name);
				
			}
			
			ArrayList<String> name_list = new ArrayList<>();
			
			for (String name : name_set) {
				name_list.add(name);
			}

				
			// 정렬
			name_list.sort((a, b) -> {
				if (a.length() != b.length()) {
					return a.length() - b.length();
				}
				
				return a.compareTo(b);
			}
			);
			
			for (String name : name_list) {
				sb.append(name).append("\n");
			}			
		}
		System.out.print(sb);
	}

}
