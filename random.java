public class random {
    
}
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String s = "abcabcbb";
        Map<Character, Integer> countMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            // Update count
            countMap.put(ch, countMap.getOrDefault(ch, 0) + 1);

            // Print only when it's the SECOND occurrence
            if (countMap.get(ch) == 2) {
                System.out.println("Second occurrence of '" + ch + "' is at index: " + i);
            }
        }
    }
}
