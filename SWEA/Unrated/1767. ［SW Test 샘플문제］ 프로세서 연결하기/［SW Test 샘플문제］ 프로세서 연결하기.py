import java.io.*;
import java.util.*;

public class Solution {
	static int[][] grid;
	static int N;
	static ArrayList<int[]> processorList = new ArrayList<>();
	
	static int[] di = {-1, 1, 0, 0};
	static int[] dj = {0, 0, -1, 1};
	
	public static void main(String arts[]) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			sb.append("#").append(tc + 1).append(" ");
			
			int n = Integer.parseInt(br.readLine());
			N = n;
			
			grid = new int[N][N];
			processorList = new ArrayList<>();
			
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				
				for (int j = 0; j < N; j++) {
					grid[i][j] = Integer.parseInt(st.nextToken());
					
					// 프로세서 위치 저장
					if (grid[i][j] == 1) {
						processorList.add(new int[] {i, j});
					}
				}
			}
			
			int[][] copied = new int[N][N];
			
			for (int i = 0; i < N; i++) {
				copied[i] = grid[i].clone();
			}
			
			max_connected = 0;
			numOfLine = Integer.MAX_VALUE;
			
			recursive(copied, 0, 0, 0);

			sb.append(numOfLine).append("\n");
			
		}
		
		System.out.print(sb);
	}
	
	static int max_connected;
	static int numOfLine;
	
	static private void recursive(int[][] arr, int connected_p, int connected_line, int idx) {
		
		// 종료조건
		if (idx == processorList.size()) {
			if (connected_p > max_connected) {
				max_connected = connected_p;
				numOfLine = connected_line;
			} else if (connected_p == max_connected) {
				numOfLine = Math.min(numOfLine, connected_line);
			}
			return;
		}
			
		int[] pos = processorList.get(idx);
		
		int ni = pos[0];
		int nj = pos[1];
		
		// 가장자리에 있는 프로세서
		if (ni == 0 || ni == N-1 || nj == 0 || nj == N-1) {
			recursive(arr, connected_p + 1, connected_line, idx + 1);
		} else {
		
			for (int k = 0; k < 4; k++) {
				
				if (validate(ni, nj, k, arr)) {
					
					// 주어진 배열 복사
					int[][] copied = new int[N][N];
					
					for (int l = 0; l < N; l++) {
						copied[l] = arr[l].clone();
					}
					
					int tempNi = pos[0];
					int tempNj = pos[1];
					int addLine = 0;
					
					// 이동하면서 전선개수 추가 및 전선 표시					
					while (true) {
						
						tempNi += di[k];
						tempNj += dj[k];
						
						if (tempNi < 0 || tempNi >= N || tempNj < 0 || tempNj >= N) break;
						
						copied[tempNi][tempNj] = 2;
						addLine++;
						
					}
					
					recursive(copied, connected_p + 1, connected_line + addLine, idx + 1);
				}
			}
			// 프로세서 연결하지 않는 경우
			recursive(arr, connected_p, connected_line, idx + 1);
		}
	}
	
	static private boolean validate(int i, int j, int d, int[][] arr) {
		
		int ni = i;
		int nj = j;
		
		while (true) {
			
			ni += di[d];
			nj += dj[d];
			
			if (ni < 0 || ni >= N || nj < 0 || nj >= N) {
				return true;
			}
			
			if (arr[ni][nj] != 0) {
				return false;
			}
		}
	}
	
}
