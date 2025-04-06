
// GCD Euclid
// Difficulty: BasicAccuracy: 67.62%Submissions: 11K+Points: 1Average Time: 15m
// You are given two numbers a and b. Find their GCD using recursion.

// Example 1:

// Input:
// a = 7, b = 8
// Output: 1
// Example 2:

// Input:
// a = 2, b = 4
// Output: 2


class Solution
{
    // Complete the function
    // a: first number
    // b: second number
    public static int GCD(int a, int b)
    {
        // find and return GCD of two numbers;
        if(b==0){
            return a;
        }
        
        return GCD(b,a%b);
    }
}


// This implementation of the GCD function uses the Euclidean Algorithm, which is an efficient method for finding the Greatest Common Divisor (GCD) of two numbers. The core idea is that the GCD of two numbers a and b is the same as the GCD of b and a % b, and this process is repeated recursively until b becomes zero. At that point, a is the GCD. For example, to find the GCD of 7 and 8, we perform the following steps: GCD(7, 8) becomes GCD(8, 7) → GCD(7, 1) → GCD(1, 0), and we return 1. This means 7 and 8 are coprime (they have no common divisor other than 1). This algorithm is both simple and efficient, making it ideal for problems involving divisibility and number theory.

