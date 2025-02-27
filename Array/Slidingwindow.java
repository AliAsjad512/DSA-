import java.util.*;

public class SlidingWindow {
    // Returns maximum sum in a subarray of size k.
    public static int maxSum(int[] arr, int n, int k) {
        // n must be greater
        if (n < k) {
            System.out.println("Invalid");
            return -1;
        }

        // Sum of first window of size k
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }

        // Compute sums of remaining windows by
        // removing first element of previous
        // window and adding last element of
        // current window.
        int maxSum = windowSum;
        for (int i = k; i < n; i++) {
            windowSum += arr[i] - arr[i - k];
            maxSum = Math.max(maxSum, windowSum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        int n = 6, k = 3;
        int[] arr = {16, 12, 9, 19, 11, 8};
        System.out.println(maxSum(arr, n, k));
    }
}
