import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().toLowerCase();

        int vowels = 0, consonants = 0;
        String vowelStr = "aeiou";

        for(char ch : s.toCharArray()){
            if(Character.isLetter(ch)){
                if(vowelStr.indexOf(ch) != -1) vowels++;
                else consonants++;
            }
        }

        System.out.println("Vowels: " + vowels);
        System.out.println("Consonants: " + consonants);
    }
}
