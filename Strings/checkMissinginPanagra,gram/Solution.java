// package Strings.checkMissinginPanagra,gram;
// import java.util.*;
// import java.util.concurrent.LinkedBlockingQueue;
// public class Solution {
//     public static String missingPanagram(String str)
//     {
//         // Find and return the missing characters
//          if (str == null || str.isEmpty()) {
//             return "-1"; // Return "-1" if the string is empty or null
//         }
        
//         // Create a set to track existing characters
//         HashSet<Character> set = new HashSet<>();
       
//         // Convert all alphabets into lowercase
//         str = str.toLowerCase();
        
//         // Add each character in the string to the set (ignoring duplicates)
//         for (int i = 0; i < str.length(); i++) {
//             set.add(str.charAt(i));
//         }
        
//         // Store missing alphabets into a StringBuilder
//         StringBuilder missing = new StringBuilder();
        
//         // Loop through all alphabets ('a' to 'z')
//         for (char c = 'a'; c <= 'z'; c++) {
//             // If the character is not present in the set, append it to the result
//             if (!set.contains(c)) {
//                 missing.append(c);
//             }
//         }
        
//         // If there are no missing characters, return "-1" (it's a pangram already)
//         if (missing.length() == 0) {
//             return "-1"; // This indicates the string is already a pangram
//         }
        
//         // Return the missing characters as a string
//         return missing.toString();
//     }
        
    
// }









/////1




//User function Template for Java


// class Solution {
//     // Complete the function
//     // str: input string
//     public static String missingPanagram(String str) {
//         // Create a boolean array to keep track of the alphabet
//         boolean[] present = new boolean[26];
        
//         // Mark the characters present in the string
//         for (char ch : str.toLowerCase().toCharArray()) {
//             if (ch >= 'a' && ch <= 'z') {
//                 present[ch - 'a'] = true;
//             }
//         }
        
//         // Collect missing characters
//         StringBuilder missingChars = new StringBuilder();
//         for (int i = 0; i < 26; i++) {
//             if (!present[i]) {
//                 missingChars.append((char) (i + 'a'));
//             }
//         }
        
//         // If no missing characters, return -1
//         return missingChars.length() == 0 ? "-1" : missingChars.toString();
//     }
// }






///2


//User function Template for Java


// class Solution
// {
//     // Complete the function
//     // str: input string
//     public static String missingPanagram(String str)
//     {
//         HashSet<Character> t=new HashSet<>();
//         for(int i=0;i<str.length();i++)
//         {
//             char c=str.charAt(i);
//             if(c>='a' && c<='z')
//             {
//                 t.add(c);
//             }
//             else if(c>='A' && c<='Z')
//             {
//                 t.add(Character.toLowerCase(c));
//             }
//         }
        
//         StringBuilder sb=new StringBuilder();
//         for(char c='a';c<='z';c++)
//         {
//             if(!t.contains(c))
//             {
//                 sb.append(c);
//             }
//         }
//         if(sb.length()==0)
//         {
//             return "-1";
//         }
//         else
//         {
//        return(sb.toString());
//         // Find and return the missing characters
//         // to complete Panagram string
//     }
// }
// }






///3
/// 



//User function Template for Java


// class Solution
// {
//     // Complete the function
//     // str: input string
//     public static String missingPanagram(String str)
//     {
//         // Find and return the missing characters
//         // to complete Panagram string
        
//         int[] freq = new int[26];
//         for(char c : str.toLowerCase().toCharArray()) {
//             freq[c-'a']++;
//         }
        
//         StringBuilder sb = new StringBuilder();
//         for(int i=0;i<26;i++) {
//             if(freq[i] == 0)
//                 sb.append((char)(i+'a'));
//         }
        
//         if(sb.length() == 0)
//             return "-1";
//         return sb.toString();
//     }
// }