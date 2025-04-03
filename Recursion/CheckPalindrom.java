// Check Palindrome
// Difficulty: EasyAccuracy: 49.98%Submissions: 23K+Points: 2Average Time: 15m
// You are given a number n. You need to see if the number is a palindrome or not (recursively)

// Example 1:

// Input:
// n = 100
// Output: 0
// Example 2:

// Input:
// n = 101
// Output: 1

class Solution
{
    
    static int reverseHelper(int N, int reversed){
        if(N==0){
            return reversed;
        }
        int lastDigit = N%10;
        reversed = reversed*10 + lastDigit;
        return reverseHelper(N/10,reversed);
    }
    // Complete the function
    // N: input element
    static boolean isPalin(int N)
    {
        // Check if the number is palindrome or not
        //You may use a helper function if you like
        return N == reverseHelper(N,0);
    }
    
    
    
}