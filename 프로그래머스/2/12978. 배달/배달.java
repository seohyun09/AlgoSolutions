import java.util.*;

class Solution {
    static int N;
    static Map<Integer, List<int[]>> graph;
    
    public int solution(int N, int[][] road, int K) {
        this.N = N;
        
        // 인접행렬
        graph = new HashMap<>();
        for (int i = 0; i < N + 1; i++) {
            graph.put(i, new ArrayList<>());
        }
        
        for (int i = 0; i < road.length; i++) {
            int s = road[i][0];
            int e = road[i][1];
            int w = road[i][2];
            
            graph.get(s).add(new int[] {e, w});
            graph.get(e).add(new int[] {s, w});
        }
        
        int[] D = dijkstra(1);
        int answer = 0;
        
        for (int i = 1; i < N + 1; i++) {
            if (D[i] <= K) answer++;
        }
        
        return answer;
    }
    private int[] dijkstra(int start) {
        int[] D = new int[N + 1];
        
        // 거리 배열 초기화
        for (int i = 1; i < N + 1; i++) {
            D[i] = Integer.MAX_VALUE;
        }
        
        D[start] = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));
        pq.add(new int[] {0, start});
        
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            
            int w = curr[0];
            int node = curr[1];
            
            if (w > D[node]) continue;
            
            for (int[] next : graph.getOrDefault(node, new ArrayList<>())) {
                int next_node = next[0];
                int next_weight = next[1];
                
                int new_distance = w + next_weight;
                
                if (new_distance < D[next_node]) {
                    D[next_node] = new_distance;
                    pq.add(new int[] {new_distance, next_node});
                }
                
            }
        }
        return D;
    }
}