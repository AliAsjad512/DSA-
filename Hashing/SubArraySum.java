package Hashing;

import java.util.HashMap;

public class SubArraySum {
    public static boolean hasZeroSumSubarray(int[] arr) {
        // Create a hash map to store the cumulative sum and its index
        HashMap<Integer, Integer> map = new HashMap<>();
        int cumulativeSum = 0;

        for (int i = 0; i < arr.length; i++) {
            cumulativeSum += arr[i];
         System.out.println(cumulativeSum);
            // Check if cumulative sum is zero or exists in the hash map
            if (cumulativeSum == 0 || map.containsKey(cumulativeSum)) {
                return true; // Found a subarray with sum 0
            }

            // Store the cumulative sum in the map
            map.put(cumulativeSum, i);
              System.out.println(map);
        }
      

        return false; // No subarray with sum 0 found
    }
     

    public static void main(String[] args) {
        int[] arr = {1,4,13,-3,-10,5};

        if (hasZeroSumSubarray(arr)) {
            System.out.println("Subarray with sum 0 exists.");
        } else {
            System.out.println("No subarray with sum 0 exists.");
        }
    }
    
}




// Let's break it down carefully to understand why having 5 in the HashMap tells us that the subarray has the given sum (4). Here's the step-by-step explanation:

// Step 1: Understanding the Equation
// We are working with the key equation:

// cumulativeSum[j]
// −
// targetSum
// =
// cumulativeSum[i-1]
// cumulativeSum[j]−targetSum=cumulativeSum[i-1]
// This equation says:

// If we can find a previous cumulative sum (
// cumulativeSum[i-1]
// cumulativeSum[i-1]) in the HashMap, it means that the subarray starting from index 
// 𝑖
// i to 
// 𝑗
// j has the sum equal to the target sum.
// Step 2: What is happening at Index 3?
// Given values:

// cumulativeSum[3]
// =
// 9
// cumulativeSum[3]=9 (sum of elements from index 0 to 3)
// targetSum
// =
// 4
// targetSum=4
// We calculate:

// cumulativeSum[3]
// −
// targetSum
// =
// 9
// −
// 4
// =
// 5
// cumulativeSum[3]−targetSum=9−4=5
// The value 
// 5
// 5 is found in the HashMap, and it corresponds to 
// cumulativeSum[0]
// cumulativeSum[0].

// Step 3: Why does this tell us the subarray has the given sum?
// Since 
// 5
// =
// cumulativeSum[0]
// 5=cumulativeSum[0], it means:

// The sum of elements from index 0 to 0 is 
// 5
// 5.
// The sum of elements from index 0 to 3 is 
// 9
// 9.
// The difference between these two cumulative sums gives the sum of the subarray from index 1 to 3:

// sum(arr[1..3])
// =
// cumulativeSum[3]
// −
// cumulativeSum[0]
// =
// 9
// −
// 5
// =
// 4
// sum(arr[1..3])=cumulativeSum[3]−cumulativeSum[0]=9−5=4
// Thus, the subarray {3, 2, -1} has a sum of 
// 4
// 4, which matches the target.

// Step 4: How the HashMap Helps
// The HashMap stores the cumulative sums as you traverse the array. By checking if 
// cumulativeSum[j]
// −
// targetSum
// cumulativeSum[j]−targetSum exists in the HashMap:

// You can instantly determine if there is a previous subarray whose sum, when subtracted from the current cumulative sum, equals the target sum.
// This eliminates the need to check all possible subarrays manually.

