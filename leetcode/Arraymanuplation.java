import java.util.*;

public class ArrayManipulation {
    public static long arrayManipulation(int n, int[][] queries) {
        long[] diff = new long[n + 2]; // use long because k can be up to 1e9

        // Apply difference array updates
        for (int[] query : queries) {
            int a = query[0];
            int b = query[1];
            int k = query[2];
            diff[a] += k;
            diff[b + 1] -= k;
        }

        // Compute prefix sum and track max
        long maxVal = 0;
        long current = 0;
        for (int i = 1; i <= n; i++) {
            current += diff[i];
            if (current > maxVal) {
                maxVal = current;
            }
        }

        return maxVal;
    }

    public static void main(String[] args) {
        int n = 5;
        int[][] queries = {
            {1, 2, 100},
            {2, 5, 100},
            {3, 4, 100}
        };

        System.out.println(arrayManipulation(n, queries)); // Output: 200
    }
}
