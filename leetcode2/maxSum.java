// Sliding Window Example
// Problem: Find the maximum sum of any contiguous subarray of size K
// Author: Ali
// Date: October 2025

public class MaxSubarraySumSlidingWindow {

    // Function to calculate maximum subarray sum of size k
    public static int maxSubarraySum(int[] arr, int k) {
        if (arr.length < k) {
            throw new IllegalArgumentException("Array size must be greater than or equal to K");
        }

        int windowSum = 0;
        int maxSum;

        // Compute sum of first window of size k
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }

        maxSum = windowSum;

        // Slide the window from start to end of the array
        for (int i = k; i < arr.length; i++) {
            // Subtract element going out of the window and add new element
            windowSum += arr[i] - arr[i - k];
            maxSum = Math.max(maxSum, windowSum);
        }

        return maxSum;
    }

    // Main method to test the function
    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};
        int k = 3;

        int result = maxSubarraySum(arr, k);
        System.out.println("Maximum sum of a subarray of size " + k + " is: " + result);
    }
}
