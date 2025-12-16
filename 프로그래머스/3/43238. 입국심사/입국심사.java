import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long start = 0;
        long end = maxFunc(times) * n;
        long mid = (start + end) / 2;
        
        long numOfPeople = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            numOfPeople = 0;
            for (int i = 0; i < times.length; i++) { 
                numOfPeople += (mid / times[i]);
            }
            if (numOfPeople < n) {
                start = mid + 1;
            } else if (numOfPeople >= n) {
                end = mid - 1;
            }
        }
        return start;
    }
    private long maxFunc(int[] arr) {
        int maxValue = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (maxValue > arr[0]) {
                maxValue = arr[0];
            }
        }
        return maxValue;
    }
}