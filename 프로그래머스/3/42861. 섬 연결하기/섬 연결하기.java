import java.util.*;

class Edge implements Comparable<Edge> {
    int start;
    int end;
    int weight;
    
    Edge(int start, int end, int weight) {
        this.start = start;
        this.end = end;
        this.weight = weight;
    }
    
    @Override
    public int compareTo(Edge other) {
        return Integer.compare(this.weight, other.weight);
    }
}

class Solution {
    private int[] PARENT;
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        List<Edge> linked_list = new ArrayList<Edge>();
        
        for (int[] cost : costs) {
            Edge edge = new Edge(cost[0], cost[1], cost[2]);
            linked_list.add(edge);
        }
        
        // 가중치 기준 오름차순 정렬
        Collections.sort(linked_list);       
        
        // 부모 노드 설정(초기화)
        PARENT = new int[n];
        for (int i = 0; i < n; i++) {
            PARENT[i] = i;
        }
        
        for (Edge edge : linked_list) {
            int start = edge.start;
            int end = edge.end;
            int weight = edge.weight;
            
            if (union(start, end)) { // 사이클이 생기지 않는 경우
                answer += weight;
            }
        }
        
        return answer;
    }
    
    private boolean union(int a, int b) {
        if (find(a) != find(b)) {
            PARENT[find(b)] = find(a);
            return true;
        }
        return false;
    }
    
    private int find(int a) {
        if (PARENT[a] == a) {
            return a;
        }
        return find(PARENT[a]);
    }
}

