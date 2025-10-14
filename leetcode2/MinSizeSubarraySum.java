// Sliding Window Example
// Problem: Given an array of positive integers and a target sum,
// find the minimal length of a contiguous subarray whose sum ≥ target
// Author: Ali
// Date: October 2025

public class MinSizeSubarraySum {

    public static int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int windowSum = 0;
        int minLength = Integer.MAX_VALUE;

        for (int right = 0; right < nums.length; right++) {
            windowSum += nums[right];

            // Shrink the window as long as the sum >= target
            while (windowSum >= target) {
                minLength = Math.min(minLength, right - left + 1);
                windowSum -= nums[left];
                left++;
            }
        }

        return (minLength == Integer.MAX_VALUE) ? 0 : minLength;
    }

    public static void main(String[] args) {
        int[] nums = {2, 3, 1, 2, 4, 3};
        int target = 7;
        int result = minSubArrayLen(target, nums);

        System.out.println("Minimum length of subarray with sum ≥ " + target + " is: " + result);
    }
}
