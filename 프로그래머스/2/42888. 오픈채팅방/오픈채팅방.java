import java.util.*;

class Solution {
    private String ENTER = "님이 들어왔습니다.";
    private String LEAVE = "님이 나갔습니다.";
    
    public String[] solution(String[] record) {
        
        Map<String, String> NickNameMap = new HashMap<>();
        ArrayList<String[]> log = new ArrayList<>();
        
        for (String line : record) {
            String[] splited = line.split(" ");
            String status = splited[0];
            String id = splited[1];
            
            if (status.equals("Enter")) {
                String nickname = splited[2];
                NickNameMap.put(id, nickname);
                
                String[] content = {status, id};
                log.add(content);
                
            } else if (status.equals("Leave")) {
                String[] content = {status, id};
                log.add(content);
                
            } else if (status.equals("Change")) {
                String nickname = splited[2];
                NickNameMap.put(id, nickname);
            }
        }
        
        String[] answer = new String[log.size()];
        
        for (int i = 0; i < log.size(); i++) {
            String[] content = log.get(i);
            String status = content[0];
            String id = content[1];
            String result = "";
            
            String nickname = NickNameMap.get(id);
            String line;
            
            if (status.equals("Enter")) {
                line = nickname + ENTER;
            } else {
                line = nickname + LEAVE;
            }
            
            answer[i] = line;
        }
        return answer;
    }
}