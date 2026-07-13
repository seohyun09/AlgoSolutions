import java.util.*;

class Solution {
    private static int BASE_TIME;
    private static int BASE_RATE;
    private static int UNIT_TIME;
    private static int UNIT_RATE;
    
    public int[] solution(int[] fees, String[] records) {
        BASE_TIME = fees[0];
        BASE_RATE = fees[1];
        UNIT_TIME = fees[2];
        UNIT_RATE = fees[3];
        
        Map<String, String> car_in = new HashMap<>();
        Map<String, Integer> parking = new HashMap<>();
        
        for (String record : records) {
            String[] splited = record.split(" ");
            String time = splited[0];
            String car_number = splited[1];
            String status = splited[2];
            
            if (status.equals("IN")) {
                car_in.put(car_number, time);
            } else {
                String in_time = car_in.get(car_number);
                String[] time_splited = in_time.split(":");
                
                int h = Integer.parseInt(time_splited[0]);
                int m = Integer.parseInt(time_splited[1]);
                
                String[] out_time = time.split(":");
                
                int out_h = Integer.parseInt(out_time[0]);
                int out_m = Integer.parseInt(out_time[1]);
                
                parking.put(car_number, parking.getOrDefault(car_number, 0) +
                                        out_h * 60 + out_m - h * 60 - m);
                
                car_in.remove(car_number);
                
            }              
        }
        
        if (!car_in.isEmpty()) {
            for (Map.Entry<String, String> entry : car_in.entrySet()) {
                String car_number = entry.getKey();
                String in_time = entry.getValue();

                String[] time_splited = in_time.split(":");

                int h = Integer.parseInt(time_splited[0]);
                int m = Integer.parseInt(time_splited[1]);

                parking.put(car_number, parking.getOrDefault(car_number, 0) +
                                        23 * 60 + 59 - h * 60 - m);

            }
        }
        
        Map<String, Integer> parking_fee = new HashMap<>();
        List<String> carNumber = new ArrayList<>();
        
        int[] answer = new int[parking.size()];
        
        for (Map.Entry<String, Integer> entry : parking.entrySet()) {
            String car_number = entry.getKey();
            int time = entry.getValue();
            carNumber.add(car_number);
            
            if (time <= BASE_TIME) {
                parking_fee.put(car_number, BASE_RATE);
            } else {
                parking_fee.put(car_number, BASE_RATE + ((time - BASE_TIME + UNIT_TIME - 1) / UNIT_TIME) * UNIT_RATE);
            }
        }
        
        Collections.sort(carNumber);
        
        for (int i = 0; i < carNumber.size(); i++) {
            answer[i] = parking_fee.get(carNumber.get(i));
        }
        
        return answer;
    }
}