class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int row_size = arr1.length;
        int col_size = arr2[0].length;
        
        int[][] result = new int[row_size][col_size];

        for (int i = 0; i < arr1.length; i++) {
            int[] a = arr1[i];
            
            for (int j = 0; j < arr2[0].length; j++) {
                int sum = 0;
                
                for (int row = 0; row < arr2.length; row++) {
                    sum += a[row] * arr2[row][j];
                }
                result[i][j] = sum;
            }
        }
        return result;
    }
}