import java.util.*;

class Node {
    int idx;
    String city;

    Node(int idx, String city) {
        this.idx = idx;
        this.city = city;
    }
}

class Solution {
    public int solution(int cacheSize, String[] cities) {
        
        PriorityQueue<Node> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.idx, b.idx)
        );
        
        int time = 0;
        
        if (cacheSize == 0) return cities.length * 5;
        
        for (int i = 0; i < cities.length; i++) {
            String city = cities[i].toLowerCase();
            
            if (pq.isEmpty()) {
                time += 5;
                pq.offer(new Node(i, city));
            } else {
                
                Node found = null;
                
                for (Node node : pq) {
                    if (node.city.equals(city)) {
                        found = node;
                        break;
                    }
                }
                
                // cache hit
                if (found != null) {
                    time++;
                    
                    pq.remove(found);
                    pq.offer(new Node(i, city));
                }
                // cache miss
                else {
                    
                    time += 5;
                    
                    if (pq.size() == cacheSize) {
                        pq.poll();
                    }
                    
                    pq.offer(new Node(i, city));
                }
            }
            
        }
        return time;
    }
}