import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        HashMap<Character, Integer> map = new HashMap<>();

        for(char ch : s.toCharArray()){
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            if(entry.getValue() > 1){
                System.out.println(entry.getKey() + " = " + entry.getValue());
            }
        }
    }
}
