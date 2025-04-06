// Print Array Elements Using Recursion
// Difficulty: BasicAccuracy: 56.49%Submissions: 15K+Points: 1
// You are given an array arr of size n. You need to print the array elements from start to end using given recursive function.


// Example 1:

// Input:
// n = 5
// arr[] = {1,2,3,4,5}
// Output: 1 2 3 4 5

// Example 2:

// Input:
// n = 4
// arr[] = {5,4,2,1}
// Output: 5 4 2 1


class Solution {
    // Complete the function
    // arr[]: input array
    // n: size of input array
    public static void printArrayRecursively(int arr[], int n) {
        // Base case: if n is 0, return
        if (n == 0) {
            return;
        }

        // Recursively print first (n-1) elements
        printArrayRecursively(arr, n - 1);

        // Then print the nth element (index n-1)
        System.out.print(arr[n - 1] + " ");
    }
}



Here’s what happens step-by-step:

The function is first called with n = 4. It calls itself with n = 3.

With n = 3, it calls itself again with n = 2.

With n = 2, it calls itself again with n = 1.

With n = 1, it calls itself again with n = 0.

Now n = 0, so it hits the base case and returns without printing.

Going back to n = 1: prints arr[0] → 5

Then n = 2: prints arr[1] → 4

Then n = 3: prints arr[2] → 3

Then n = 4: prints arr[3] → 2