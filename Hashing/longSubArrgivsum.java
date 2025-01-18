package Hashing;
import java.util.HashMap;

class Main {
    public static int SubarrayWithGivenSum(int[] arr, int targetSum) {
        // HashMap to store cumulative sum and its corresponding index
        HashMap<Integer, Integer> map = new HashMap<>();
        int cumulativeSum = 0;
        int max = 0;

        // Iterate through the array
        for (int i = 0; i < arr.length; i++) {
            cumulativeSum += arr[i];

            // Check if the entire array up to this index sums to the target
            if (cumulativeSum == targetSum) {
                max = Math.max(max, i + 1);
            }

            // Check if (cumulativeSum - targetSum) exists in the HashMap
            if (map.containsKey(cumulativeSum - targetSum)) {
                int length = i - map.get(cumulativeSum - targetSum);
                max = Math.max(max, length);
            }

            // Store the cumulative sum with its corresponding index if not already present
            map.putIfAbsent(cumulativeSum, i);
        }

        return max; // Return the length of the longest subarray
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 0, 1, 8, 2, 3, 6};
        int targetSum = 5;

        int result = SubarrayWithGivenSum(arr, targetSum);
        System.out.println("Length of the longest subarray: " + result);
    }
}
