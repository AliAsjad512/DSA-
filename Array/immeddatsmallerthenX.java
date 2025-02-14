// Find Immediate Smaller Than X
// Difficulty: EasyAccuracy: 39.03%Submissions: 53K+Points: 2Average Time: 15m
// Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.

 

// Example 1:

// Input:
// N = 5
// arr[] = {4 67 13 12 15}
// X = 16
// Output: 15
// Explanation: For a given value 16, there
// are four values which are smaller than
// it. But 15 is the number which is smaller
// and closest to it with minimum difference
// of 1.
 

// Example 2:

// Input:
// N = 5
// arr[] = {1 2 3 4 5}
// X = 1
// Output: -1
// Explanation: No value is smaller than 1.



class Solution
{
    // Complete the function
    public static int immediateSmaller(int arr[], int n, int x)
    {
        // Your code here
        Arrays.sort(arr);
        int element=-1;
        ;
        for(int i=0;i<arr.length;i++){
            if(arr[i] < x){
               element=arr[i];
            }
            
        }
    
   
    
        return element;
    }
}
 