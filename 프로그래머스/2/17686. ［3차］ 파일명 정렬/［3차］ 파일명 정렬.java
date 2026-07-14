import java.util.*;

class Node {
    String head;
    int num;
    String number;
    String tail;
    
    Node(String head, int num, String number, String tail) {
        this.head = head;
        this.num = num;
        this.number = number;
        this.tail = tail;
    }
}

class Solution {
    public String[] solution(String[] files) {
        
        Node[] nodes = new Node[files.length];
        
        String[] answer = new String[files.length];
        int i = 0;
        
        for (String file : files) {
            int idx = 0;
            String head = "";
            
            // 문자열 저장
            while (true) {
                char c = file.charAt(idx);
                
                if (Character.isDigit(c)) {
                    break;
                } else {
                    head += String.valueOf(c);
                }
                
                idx++;
            }
            
            // 숫자 저장
            String number = "";
            
            while (idx < file.length()) {
                char c = file.charAt(idx);
                
                if (Character.isDigit(c)) {
                    number += c;
                } else {
                    break;
                }
                idx++;
            }
            
            int num = Integer.parseInt(number);
            
            String tail = file.substring(idx);
            
            nodes[i] = new Node(head, num, number, tail);
            i++;
        }
        
        Arrays.sort(nodes, (a, b) -> {
            int headCompare = a.head.compareToIgnoreCase(b.head);
            if (headCompare != 0) return headCompare;
            return a.num - b.num;
        });
        
        for (int j = 0; j < files.length; j++) {
            answer[j] = nodes[j].head + nodes[j].number + nodes[j].tail;
        }
        
        return answer;
    }
}