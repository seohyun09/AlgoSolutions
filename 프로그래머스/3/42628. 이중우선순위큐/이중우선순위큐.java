import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int i = 0; i < operations.length; i++) {
            if (operations[i].equals("D 1")) {
                if (!maxHeap.isEmpty()) {
                    int maxValue = maxHeap.poll();
                    minHeap.remove(maxValue);
                }
                
                continue;
            }
            if (operations[i].equals("D -1")) {
                if (!minHeap.isEmpty()) {
                    int minValue = minHeap.poll();
                    maxHeap.remove(minValue);
                }
                continue;
            }
            String[] parts = operations[i].split(" ");
            int num = Integer.parseInt(parts[1]);
            maxHeap.add(num);
            minHeap.add(num);
        }
        
        if (!maxHeap.isEmpty()) {
            int maxValue = maxHeap.peek();
            int minValue = minHeap.peek();
            return new int[] {maxValue, minValue};
        }
        return new int[] {0, 0};
    }
}