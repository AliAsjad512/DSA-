// package Strings.Maxfrq;
// import java.util.HashMap;

// public class Maxfrq {
//     public static char getMaxOccuringChar(String s) {
//     HashMap<Character, Integer> freqMap = new HashMap<>();
        
//         // Variable to store the maximum frequency
//         int maxFreq = 0;
//         // Variable to store the character with the maximum frequency
//         char maxChar = '\0';
        
//         // Count the frequency of each character
//         for (int i = 0; i < s.length(); i++) {
//             char ch = s.charAt(i);
//             freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
            
//             // Check if this character has a higher frequency, or if it's the same frequency but lexicographically smaller
//             int currentFreq = freqMap.get(ch);
//             if (currentFreq > maxFreq || (currentFreq == maxFreq && ch < maxChar)) {
//                 maxFreq = currentFreq;
//                 maxChar = ch;
//             }
//         }
        
//         return maxChar;
//     }
//     public static void main(String[] args) {
//         String s = "aabbbcc";
//         System.out.println(getMaxOccuringChar(s));  // Output: 'b'
//     }
    
// }



//My solution



// class Solution {
//     // Function to find the maximum occurring character in a string.
//     public static char getMaxOccuringChar(String s) {
//         StringBuilder str = new StringBuilder();
//         HashMap<Character, Integer> freqMap = new HashMap<>();
//             int max=1;
//         // Count the frequency of each character
//         for (int i = 0; i < s.length(); i++) {
//             char ch = s.charAt(i);
//             freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
//              max=Math.max(freqMap.get(ch),max);
//         }


//         // Print the frequency of each character
//         for (char ch : freqMap.keySet()) {
           
//        if(freqMap.get(ch)==max){
//            str.append(ch);
//        }
            
//         }
            
     
    
//     char j=str.charAt(0);
//         for (int i = 1; i < str.length(); i++) {
//     if(str.charAt(i) < j){
//         j=str.charAt(i);
//     }
   
   
// }
        
        
        
//         return j;
//     }
// }








// class Solution {
//     // Function to find the maximum occurring character in a string.
//     public static char getMaxOccuringChar(String s) {
//         // Your code here
        
//         // char arr[]=s.toCharArray();
//         // Arrays.sort(arr);
//         // int count =0;
//         // char c=arr[0];
//         // int i=1;
//         // int max=0;
//         // char f=c;
//         // while(i<s.length()){
//         //     if(c==arr[i]){
//         //         count++;
//         //     }
//         //     else{
//         //         if(count>max){
//         //             f=c;
//         //             max=count;
//         //         }
//         //         c=arr[i];
//         //         count=0;
//         //     }
//         //     i++;
//         // }
//         // if(count>max){
//         //     return c;
//         // }
//         // return f;
        
//         int max=0;
//         char res=s.charAt(0);
//         int n=s.length();
//         HashMap<Character,Integer> map=new HashMap<>();
//         for(int i=0;i<n;i++){
//             char ch=s.charAt(i);
//             map.put(ch,map.getOrDefault(ch,0)+1);
//             if(map.get(ch)>max){
//                 max=map.get(ch);
//                 res=ch;
//             }
//             if(map.get(ch)==max && ch<res){
//                 res=ch;
//             }
//         }
//         return res;
//     }
// }










// class Solution {
//     // Function to find the maximum occurring character in a string.
//     public static char getMaxOccuringChar(String s) {
//         // Your code here
//         char arr[]=s.toCharArray();
//         Arrays.sort(arr);
//         // for(char i: arr){
//         //     System.out.println(i);
//         // }
//         int count =0;
//         char c=arr[0];
//         int i=1;
//         int max=0;
//         char f=c;
//         while(i<s.length()){
//             if(c==arr[i]){
//                 count++;
//             }
//             else{
//                 if(count>max){
//                     f=c;
//                     max=count;
//                 }
//                 c=arr[i];
//                 count=0;
//             }
//             i++;
//         }
//         if(count>max){
//             return c;
//         }
//         return f;
//     }
// }











// class Solution {
//     // Function to find the maximum occurring character in a string.
//     public static char getMaxOccuringChar(String s) {
//         // Your code here
//         HashMap<Character,Integer> map = new HashMap<>();
//         int n = s.length();
//         char ans = '~';
//         if(n <= 1){
//             ans = s.charAt(0);
//         }
//         for(int i = 0;i<n;i++){
//             char ch = s.charAt(i);
//             if(map.containsKey(ch)){
//                 map.put(ch,map.get(ch) + 1);
//             }
//             else{
//                 map.put(ch,1);
//             }
//         }
        
//         int max = Integer.MIN_VALUE;
//         for(Map.Entry<Character,Integer> m: map.entrySet()){
//             if(m.getValue() > max || (m.getValue() == max && m.getKey() < ans)){
//                 ans = m.getKey();
//                 max = m.getValue();
//             }
//         }
//         return ans;
//     }
// }










// class Solution {
//     // Function to find the maximum occurring character in a string.
//     public static char getMaxOccuringChar(String s) {
//         // Your code here
        
//         int f[]=new int[26];
        
//         int n=s.length();
        
//         for(int i=0;i<n;i++){
//            f[(s.charAt(i)-'a')]++;
//         }
        
//         int m=-1;
//         int indx=-1;
        
//         for(int i=0;i<26;i++){
//             if(f[i]>m){
//                 m=f[i];
//                 indx=i;
//             }
//         }
//         return (char)(indx+'a');
//     }
// }



// Expected Approach
// Intuition
// The idea is to iterate through the string and create a hashmap where the keys are the characters in the string, and the values are the number of times that character occurs. Then, we can iterate through the hashmap to find the character with the highest value.

// Implementation
// Declare a vector of size 26 hash to store the the count of each character and initialize it with 0.
// Traverse the string and update the count of each character in the hash.
// Now iterate over the hash table.
// We keep storing the maximum value in hash table and its corresponding character.
// Return the character with maximum occurrences.

// This algorithm first counts the occurrences of each character in the string using a hashmap. Then, it finds the character with the maximum count by iterating through the key-value pairs in the hashmap and keeping track of the maximum count and corresponding character. Finally, it returns the character with the maximum count.
 

// Complexity 
// Time Complexity: O(N) since only one Array traversal is required.
// Space Complexity: O(N) since hashmap is used for storing elements, where N is the size of the string.


// 1
// class Solution {
// 2
//     // Function to find the maximum occurring character in a string.
// 3
//     public static char getMaxOccuringChar(String line) {
// 4
//         StringBuffer sb = new StringBuffer();
// 5
//         char[] s = line.toCharArray();
// 6
//         int[] arr = new int[26];
// 7
//         int max = -1;
// 8
//         char result = '\u0000';
// 9
// ​
// 10
//         // using hash table to store count of each character.
// 11
//         for (int i = 0; i < s.length; i++) {
// 12
//             char c = s[i];
// 13
//             if (c != ' ') {
// 14
//                 arr[c - 'a']++;
// 15
//             }
// 16
//         }
// 17
// ​
// 18
//         // iterating over the hash table.





// // class Solution {
// //     // Function to find the maximum occurring character in a string.
// //     public static char getMaxOccuringChar(String s) {
// //         // Your code here
// //         TreeMap<Character,Integer> map=new TreeMap<>();
        
// //         for(int i=0;i<s.length();i++)
// //         {
// //             map.put(s.charAt(i),map.getOrDefault(s.charAt(i),0)+1);
// //         }
        
// //         int max=0;
// //         char ptr=' ';
        
// //         for(int i=0;i<s.length();i++)
// //         {
// //             int m=map.get(s.charAt(i));
// //             if(m>max)
// //             {   
// //                 max=m;
// //                 ptr=s.charAt(i);
// //             }
// //             else if(m==max)
// //             {
// //                 ptr=(char)  Math.min(ptr,s.charAt(i));
// //             }
// //         }
// //         return ptr;
// //     }
// // }








// // class Solution {
// //     // Function to find the maximum occurring character in a string.
// //     public static char getMaxOccuringChar(String s) {
// //         // Your code here
// //         int[] freq = new int[26];
// //         for (int i = 0; i < s.length(); i++) {
// //             freq[s.charAt(i) - 'a']++;
// //         }
// //         int maxFreq = 0;
// //         char maxChar = 'a'; 
        
// //         for (int i = 0; i < 26; i++) {
// //             if (freq[i] > maxFreq) {
// //                 maxFreq = freq[i];
// //                 maxChar = (char) (i + 'a');
// //             } else if (freq[i] == maxFreq) {
// //                 char currentChar = (char) (i + 'a');
// //                 if (currentChar < maxChar) {
// //                     maxChar = currentChar;
// //                 }
// //             }
// //         }
        
// //         return maxChar;
// //     }
// // }








// // class Solution {
// //     // Function to find the maximum occurring character in a string.
// //     public static char getMaxOccuringChar(String s) {
// //         // Your code here\
// //     List<Integer> li = new ArrayList<>(Collections.nCopies(256, 0)); 
// //     for(int i=0;i<s.length();i++)
// //     {
// //          li.set((int)(s.charAt(i)), li.get((int)(s.charAt(i))) + 1);
// //     }
// //     int maxocc=li.indexOf(Collections.max(li));
// //     char ch=(char)maxocc;
// //     return ch;
// //     }
// // }










// // class Solution {
// //     // Function to find the maximum occurring character in a string.
// //     public static char getMaxOccuringChar(String line) {
// //         // Your code here
// //         int[] freq = new int[256];
// //         for (int i = 0; i < line.length(); i++) {
// //             freq[line.charAt(i)]++;
// //         }
// //         int maxFreq = -1;
// //         char maxChar = ' ';
// //         for (int i = 0; i < 256; i++) {
// //             if (freq[i] > maxFreq) {
// //                 maxFreq = freq[i];
// //                 maxChar = (char) i;
// //             }
// //             else if (freq[i] == maxFreq && (char) i < maxChar) {
// //                 maxChar = (char) i;
// //             }
// //         }
// //         return maxChar;
// //     }
// // }