// The Modified String
// Difficulty: EasyAccuracy: 49.86%Submissions: 29K+Points: 2
// Ishaan is playing with strings these days. He has found a new string. He wants to modify it as per the following rules to make it valid:

// The string should not have three consecutive same characters (Refer example for explanation).
// He can add any number of characters anywhere in the string. 
// Find the minimum number of characters which Ishaan must insert in the string to make it valid.

// Example 1:

// Input:
// S = aabbbcc
// Output: 1
// Explanation: In aabbbcc 3 b's occur
// consecutively, we add a 'd',and Hence,
// output will be aabbdbcc.
// Example 1:

// Input:
// S = aaaaa
// Output: 2
// Explanation:  In aaaaa 5 a's occur
// consecutively,we need to add 2 'b', and
// Hence, the output will be aababaa.


class Solution
{
    //Function to find minimum number of characters which Ishaan must insert  
    //such that string doesn't have three consecutive same characters.
    public static long modified(String a)
    {
        // Your code here
        int result=1;
        int totalInsertion=0;
        for(int i=1;i<a.length();i++){
            if(a.charAt(i) == a.charAt(i-1)){
                result++;
            }
            else{
                if(result>=3){
                    totalInsertion += (result-1)/2;
                }
                result=1;
            }
        }
        
            if(result>=3){
                    totalInsertion += (result-1)/2;
                }  
                
                return totalInsertion;
       
    }
}

// 1. Sliding Window Pattern:
// The Sliding Window technique involves keeping track of a "window" of elements (in this case, characters in the string) and moving through the string one character at a time. As you slide through the string, you maintain a count (here, result) of how many consecutive characters are identical.

// You start with the first character and initialize result to 1 (as the first character starts a sequence).
// As you iterate through the string, you check whether the current character is the same as the previous one.
// If they are the same, you increase result to keep track of the length of the current sequence.
// If they are different, you check if the current sequence length (result) is 3 or more. If so, you calculate how many insertions are required and add it to totalInsertion.
// You then reset result to 1, as a new sequence of characters begins.
// After processing all characters, you also check the last sequence (which might not have been processed yet).

// 2. Greedy Approach:
// The Greedy Approach involves making the locally optimal choice (in this case, the minimum number of insertions) at each step with the hope of finding the global optimum.

// Whenever you detect a sequence of 3 or more consecutive characters, you make the greedy decision to break it into smaller valid groups (groups of 2 consecutive characters).
// To break a sequence of length n, the number of insertions needed is (n - 1) / 2. This is because you want to break the sequence into groups of 2, and each group after the first needs an insertion to ensure no group has more than 2 consecutive identical characters.
// Code Walkthrough:
// java
// Copy code
// int result = 1;  // Start counting from the first character
// int totalInsertion = 0;  // To keep track of total insertions needed

// // Loop through the string starting from the second character
// for (int i = 1; i < a.length(); i++) {
//     // If the current character is the same as the previous one, increase the result
//     if (a.charAt(i) == a.charAt(i - 1)) {
//         result++;
//     } else {
//         // If we found a sequence of 3 or more, calculate insertions
//         if (result >= 3) {
//             totalInsertion += (result - 1) / 2;
//         }
//         result = 1;  // Reset for the new sequence of characters
//     }
// }

// // After the loop, check the last sequence
// if (result >= 3) {
//     totalInsertion += (result - 1) / 2;
// }

// return totalInsertion;  // Return the total insertions needed
// Explanation of the Code:
// result: This variable counts the length of the current sequence of consecutive identical characters.
// totalInsertion: This variable accumulates the total number of insertions required to break the sequences into valid groups.
// if (a.charAt(i) == a.charAt(i - 1)): This checks if the current character is the same as the previous one to keep track of a consecutive sequence.
// if (result >= 3): This checks if the current sequence of consecutive characters is of length 3 or more. If so, the formula (result - 1) / 2 calculates the number of insertions needed to break it into smaller valid groups.
// result = 1;: This resets the counter for a new sequence of characters.
// After the loop ends, you need to check if the final sequence (the one ending at the last character) has 3 or more characters. If so, you calculate insertions for that sequence.
// Pattern Identified:
// Sliding Window: You are "sliding" through the string and counting the length of consecutive identical characters.
// Greedy Approach: After detecting a sequence of 3 or more characters, you immediately calculate the minimum number of insertions required to split that sequence into smaller, valid groups.
// Final Thoughts:
// This is a combination of:

// Sliding Window: As you traverse through the string, you're dynamically keeping track of the length of the current sequence.
// Greedy Algorithm: You're taking the immediate optimal decision at each step (insertions) to ensure the string follows the rule of not having three consecutive characters.
// This method efficiently handles the problem with linear time complexity, making it both optimal and simple to implement.



