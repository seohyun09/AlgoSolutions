class Solution {
    static int A;
    static int B;
    
    public int solution(int n, int a, int b) {
        A = a;
        B = b;
        
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        
        return recur(arr, 0);
        
    }
    private int recur(int[] arr, int cnt) {
    
        int[] next_arr = new int[arr.length / 2];
        
        for (int i = 0; i < arr.length; i += 2) {
            
            if ((arr[i] == A && arr[i+1] == B) ||
                (arr[i] == B && arr[i+1] == A)) {
                return cnt + 1;
            }            
            
            if (arr[i] == A || arr[i+1] == A) {
                next_arr[i/2] = A;    
            } else if (arr[i] == B || arr[i+1] == B) {
                next_arr[i/2] = B;
            } else {
                next_arr[i/2] = arr[i];
            }
            
        }
        return recur(next_arr, cnt + 1);
    }
}