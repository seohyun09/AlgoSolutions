import java.util.*;

class Solution {
    static int N;
    static ArrayList<int[]>[] graph;
    
    public int solution(int n, int[][] costs) {
        N = n;
        graph = new ArrayList[N];
        
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < costs.length; i++) {
            int start = costs[i][0];
            int end = costs[i][1];
            int cost = costs[i][2];
            
            graph[start].add(new int[] {end, cost});
            graph[end].add(new int[] {start, cost});
        }
        
        return Prim(0);       
        
    }
    private int Prim(int start) {
        boolean[] mst = new boolean[N];
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0])
        );
        pq.add(new int[] {0, start});
        
        int min_w = 0;
        int cnt_v = 0;
        
        while (!pq.isEmpty() && cnt_v < N) {
            
            int[] curr = pq.poll();
            int w = curr[0];
            int v = curr[1];
            
            if (mst[v]) continue;
            
            mst[v] = true;
            min_w += w;
            cnt_v++;
            
            for (int[] edge : graph[v]) {
                int nv = edge[0];
                int nw = edge[1];
                
                pq.add(new int[] {nw, nv});
            }
            
        }
        return min_w;
    }
}
