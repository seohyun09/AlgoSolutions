import java.io.*;
import java.util.*;

public class Solution {
	// 상, 하, 좌, 우
	static int[] di = {0, -1, 1, 0, 0};
	static int[] dj = {0, 0, 0, -1, 1};
	
	public static void main(String args[]) throws Exception	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			st = new StringTokenizer(br.readLine());
			
			int n = Integer.parseInt(st.nextToken()); // 셀 개수
			int m = Integer.parseInt(st.nextToken()); // 격리 시간
			int k = Integer.parseInt(st.nextToken()); // 미생물 군집 개수
			
			// 값을 저장할 배열 초기화
			int[][] sum = new int[n][n];
			int[][] max = new int[n][n];
			int[][] maxDir = new int[n][n];
			
			// 입력
			for (int i = 0; i < k; i++) {
				st = new StringTokenizer(br.readLine());
				
				int si = Integer.parseInt(st.nextToken()); // 세로위치
				int sj = Integer.parseInt(st.nextToken()); // 가로위치
				int num = Integer.parseInt(st.nextToken()); // 미생물 수
				int dir = Integer.parseInt(st.nextToken()); // 이동방향
				
				sum[si][sj] = num;
				maxDir[si][sj] = dir;
			}			
			
			while (m!= 0) {
				
				// 값을 저장할 새 배열
				int[][] next_sum = new int[n][n];
				int[][] next_max = new int[n][n];
				int[][] next_maxDir = new int[n][n];
				
				// 방향 대로 이동
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < n; j++) {
						
						int dir = maxDir[i][j];
						int num = sum[i][j];
						
						int ni = i + di[dir];
						int nj = j + dj[dir];
						
						if (num == 0) continue;
						
						// 약품에 도달한 경우
						else if (ni == 0 || ni == n-1 || nj == 0 || nj == n-1) {
							num /= 2;
							
							if (dir == 1) dir = 2;
							else if (dir == 2) dir = 1;
							else if (dir == 3) dir = 4;
							else if (dir == 4) dir = 3;
							
							next_sum[ni][nj] += num;
							next_max[ni][nj] = num;
							next_maxDir[ni][nj] = dir;
						}
						
						// 값이 존재하는 경우
						else if (next_sum[ni][nj] > 0) {
							// 해당 값이 큰 경우, 최대값 및 방향 갱신
							if (next_max[ni][nj] < num) {
								next_max[ni][nj] = num;
								next_maxDir[ni][nj] = dir;
							}
							
							next_sum[ni][nj] += num;							
							
						} else {
							next_sum[ni][nj] = num;
							next_max[ni][nj] = num;
							next_maxDir[ni][nj] = dir;
							
						}
						
					}
				}
				
				sum = next_sum;
				max = next_max;
				maxDir = next_maxDir;
				
				m--;
			}
			
			// 남아 있는 미생물 수 확인
			int total = 0;
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (sum[i][j] > 0) {
						total += sum[i][j];
					}
				}
			}
			
			sb.append("#").append(tc + 1).append(" ").append(total).append("\n");
			
		}
		
		System.out.print(sb);
	}
}