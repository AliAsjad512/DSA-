// Sliding Window Example
// Problem: Find the length of the longest substring without repeating characters
// Author: Ali
// Date: October 2025

import java.util.HashSet;

public class LongestUniqueSubstring {

    public static int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLength = 0;
        HashSet<Character> window = new HashSet<>();

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // If character already exists, shrink the window
            while (window.contains(currentChar)) {
                window.remove(s.charAt(left));
                left++;
            }

            window.add(currentChar);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        String s = "abcabcbb";
        int result = lengthOfLongestSubstring(s);
        System.out.println("Longest substring without repeating characters: " + result);
    }
}
