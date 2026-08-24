class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        int idx = 0;
        
        for (long num : numbers) {
            answer[idx] = validate(num);
            idx++;
        }
        
        return answer;
    }
    private long validate(long num) {
        
        String binary = Long.toBinaryString(num);
        int cnt = 0;
        
        char[] arr = binary.toCharArray();
        for (char c : arr) {
            if (c == '1') cnt++;
        }
        if (cnt == binary.length()) {
            binary = "10" + binary.substring(1);
        } else {
            for (int j = binary.length() - 1; j > -1; j--) {
                if (arr[j] == '0') {
                    arr[j] = '1';
                    if (j != binary.length() - 1 && arr[j + 1] == '1') {
                        arr[j+1] = '0';
                    }
                    break;
                }
            }
            binary = new String(arr);
        }
        
        return Long.parseLong(binary, 2);
    }
}