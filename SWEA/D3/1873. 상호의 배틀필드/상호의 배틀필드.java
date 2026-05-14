import java.io.*;
import java.util.*;

public class Solution {
	static char[][] gameMap;
	static int H;
	static int W;
	static int[] di = {-1, 1, 0, 0};
	static int[] dj = {0, 0, -1, 1};
	
	public static void main(String arts[]) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int t = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < t; tc++) {
			sb.append("#").append(tc + 1).append(" ");
			st = new StringTokenizer(br.readLine());
			
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			
			gameMap = new char[H][W];
			int si = 0;
			int sj = 0;
			int dir = 0;
			
			for (int i = 0; i < H; i++) {
				gameMap[i] = br.readLine().toCharArray();
				
				for (int j = 0; j < W; j++) {
					if (gameMap[i][j] == '^' || gameMap[i][j] == 'v' ||
						gameMap[i][j] == '<' || gameMap[i][j] == '>') {
						si = i;
						sj = j;
						dir = setDir(gameMap[i][j]);
						gameMap[i][j] = '.';
					}
				}
			}
			
			int n = Integer.parseInt(br.readLine());
			String order = br.readLine();
			
			int curr_i = si;
			int curr_j = sj;
			int curr_dir = dir;
			
			for (int i = 0; i < n; i++) {
				
				char orderChar = order.charAt(i);
				
				if (orderChar == 'U') {
					curr_dir = 0;
					
					int ni = curr_i + di[0];
					int nj = curr_j + dj[0];
					
					if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
					
					if (gameMap[ni][nj] == '.') {
						curr_i = ni;
						curr_j = nj;
					} else {
						continue;
					}
					
				} else if (orderChar == 'D') {
					curr_dir = 1;
					
					int ni = curr_i + di[1];
					int nj = curr_j + dj[1];
					
					if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
					
					if (gameMap[ni][nj] == '.') {
						curr_i = ni;
						curr_j = nj;						
					} else {
						continue;
					}
					
				} else if (orderChar == 'L') {
					curr_dir = 2;
					
					int ni = curr_i + di[2];
					int nj = curr_j + dj[2];
					
					if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
					
					if (gameMap[ni][nj] == '.') {
						curr_i = ni;
						curr_j = nj;
					} else {
						continue;
					}
					
				} else if (orderChar == 'R') {
					curr_dir = 3;
					
					int ni = curr_i + di[3];
					int nj = curr_j + dj[3];
					
					if (ni < 0 || ni >= H || nj < 0 || nj >= W) continue;
					
					if (gameMap[ni][nj] == '.') {
						curr_i = ni;
						curr_j = nj;
					} else {
						continue;
					}
					
				} else if (orderChar == 'S') {
					shootFunc(curr_i, curr_j, curr_dir);
				}
				
			}
			
			gameMap[curr_i][curr_j] = setNum(curr_dir);
			
			for (int i = 0; i < H; i++) {
				String line = "";
				
				for (int j = 0; j < W; j++) {
					line += gameMap[i][j];
				}
				sb.append(line).append("\n");
			}
			
		}
		System.out.print(sb);
	}
	
	static int setDir(char target) {
		if (target == '^') return 0;
		else if (target == 'v') return 1;
		else if (target == '<') return 2;
		else if (target == '>') return 3;
		return -1;
	}
	
	static char setNum(int num) {
		if (num == 0) return '^';
		else if (num == 1) return 'v';
		else if (num ==2) return '<';
		else if (num == 3) return '>';
		return ' ';
	}
	
	static void shootFunc(int i, int j, int d) {
		
		int ni = i;
		int nj = j;
		
		while (true) {
			
			ni += di[d];
			nj += dj[d];
			
			if (ni < 0 || ni >= H || nj < 0 || nj >= W) return;
			
			if (gameMap[ni][nj] == '*') {
				gameMap[ni][nj] = '.';
				return;
			} else if (gameMap[ni][nj] == '#') {
				return;
			}
		}
	}
}
