package Strings;


// Remove common characters and concatenate
// Difficulty: BasicAccuracy: 30.78%Submissions: 72K+Points: 1
// Given two strings s1 and s2. Modify both the strings such that all the common characters of s1 and s2 are to be removed and the uncommon characters of s1 and s2 are to be concatenated.
// Note: If all characters are removed print -1.

// Example 1:

// Input:
// s1 = aacdb
// s2 = gafd
// Output: cbgf
// Explanation: The common characters of s1
// and s2 are: a, d. The uncommon characters
// of s1 and s2 are c, b, g and f. Thus the
// modified string with uncommon characters
// concatenated is cbgf.
// Example 2:

// Input:
// s1 = abcs
// s2 = cxzca
// Output: bsxz
// Explanation: The common characters of s1
// and s2 are: a,c. The uncommon characters
// of s1 and s2 are b,s,x and z. Thus the
// modified string with uncommon characters
// concatenated is bsxz.









import java.util.HashSet;
import java.util.Set;

public class removeCommonCharacter {
    
    public static String concatenatedString(String s1,String s2)
    {
        // Your code here
        Set<Character> s1Set = new HashSet<>();
        Set<Character> s2Set = new HashSet<>();
        
        // Add characters of s1 and s2 to the sets
        for (int i = 0; i < s1.length(); i++) {
            s1Set.add(s1.charAt(i));
        }
        
        for (int i = 0; i < s2.length(); i++) {
            s2Set.add(s2.charAt(i));
        }

        // Remove common characters from both sets
        Set<Character> commonChars = new HashSet<>(s1Set);
        commonChars.retainAll(s2Set);
        
        // Create result string for s1 and s2 after removing common characters
        StringBuilder result = new StringBuilder();
        
        // Process s1, adding characters that are not in commonChars
        for (int i = 0; i < s1.length(); i++) {
            if (!commonChars.contains(s1.charAt(i))) {
                result.append(s1.charAt(i));
            }
        }

        // Process s2, adding characters that are not in commonChars
        for (int i = 0; i < s2.length(); i++) {
            if (!commonChars.contains(s2.charAt(i))) {
                result.append(s2.charAt(i));
            }
        }

        // If the result is empty, print -1
        if (result.length() == 0) {
        return "-1";
        } else {
            return result.toString();
        }
      
}
}













// class Solution
// {
//     //Function to remove common characters and concatenate two strings.
//     public static String concatenatedString(String s1,String s2)
//     {
//         // HashSet<Character> common = new HashSet<>();

//         HashSet<Character> common = new HashSet<>();

//         // Add characters from s1 to HashSet
//         for (char c : s1.toCharArray()) {
//             common.add(c);  // Add each character to the set
//         }

//         // Find common characters in both strings
//         HashSet<Character> commonInBoth = new HashSet<>();
//         for (char c : s2.toCharArray()) {
//             if (common.contains(c)) {
//                 commonInBoth.add(c);  // Store common characters
//             }
//         }

//         // Build the result string
//         StringBuilder result = new StringBuilder();

//         // Add characters from s1 not in commonInBoth
//         for (char c : s1.toCharArray()) {
//             if (!commonInBoth.contains(c)) {
//                 result.append(c);
//             }
//         }

//         // Add characters from s2 not in commonInBoth
//         for (char c : s2.toCharArray()) {
//             if (!commonInBoth.contains(c)) {
//                 result.append(c);
//             }
//         }

//         // If no characters left, return -1
//         return result.length() == 0 ? "-1" : result.toString();
//     }
// }