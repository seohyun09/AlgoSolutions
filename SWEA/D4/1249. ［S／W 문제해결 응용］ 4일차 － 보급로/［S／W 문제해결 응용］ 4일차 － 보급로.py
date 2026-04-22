from heapq import heappush, heappop

t = int(input())

for tc in range(t):
	n = int(input())
	arr = [list(map(int, input().strip())) for _ in range(n)]	
	
	# 상(0), 하(1), 좌(2), 우(3)
	di = [-1, 1, 0, 0]
	dj = [0, 0, -1, 1]
	
	INF = 1e9
	
	D = [[INF] * n for _ in range(n)]
	D[0][0] = 0

	def dijkstra(si, sj):
		heap = []

		heappush(heap, (arr[0][0], si, sj))
		
		while heap:
			w, i, j = heappop(heap)
			
			for d in range(4):
				ni = i + di[d]
				nj = j + dj[d]
				
				if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
				
				new_distance = w + arr[ni][nj]
				
				if new_distance < D[ni][nj]:
					D[ni][nj] = new_distance
					
					heappush(heap, (new_distance, ni, nj))
	
	dijkstra(0, 0)
			
	print(f"#{tc + 1} {D[n-1][n-1]}")
	