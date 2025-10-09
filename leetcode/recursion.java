// LeetCode Problem: Reverse String using Recursion
// Author: Your Name
// Date: 2025-10-08

public class ReverseString {

    public static void reverseString(char[] s) {
        helper(s, 0, s.length - 1);
    }

    private static void helper(char[] s, int left, int right) {
        if (left >= right) {
            return; // base case
        }

        // swap characters
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        // recursive call
        helper(s, left + 1, right - 1);
    }

    public static void main(String[] args) {
        char[] s = {'h', 'e', 'l', 'l', 'o'};
        reverseString(s);
        System.out.println(s); // Output: olleh
    }
}
