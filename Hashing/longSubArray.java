
import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] arr = {5, 8, -4, -4, 9, -2, 2};
        int targetSum = 0;

        Map<Integer, Integer> prefixMap = new HashMap<>();
        int prefixSum = 0;
        int maxLength = 0;

        for (int i = 0; i < arr.length; i++) {
            prefixSum += arr[i];

            // Case 1: subarray [0..i]
            if (prefixSum == targetSum) {
                maxLength = i + 1;
            }

            // Case 2: subarray ending at i
            if (prefixMap.containsKey(prefixSum - targetSum)) {
                int prevIndex = prefixMap.get(prefixSum - targetSum);
                maxLength = Math.max(maxLength, i - prevIndex);
            }

            // Store first occurrence of prefixSum
            prefixMap.putIfAbsent(prefixSum, i);
        }

        System.out.println("Maximum Length Subarray with sum " + targetSum + " = " + maxLength);
    }
}

