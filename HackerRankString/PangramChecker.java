import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().toLowerCase();

        boolean[] seen = new boolean[26];
        int count = 0;

        for(char ch : s.toCharArray()) {
            if(ch >= 'a' && ch <= 'z') {
                if(!seen[ch - 'a']) {
                    seen[ch - 'a'] = true;
                    count++;
                }
            }
        }

        if(count == 26) System.out.println("pangram");
        else System.out.println("not pangram");
    }
}
