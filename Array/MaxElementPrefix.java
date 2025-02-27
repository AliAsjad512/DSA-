public class MaxElementInArray {
    public static int getMaxElement(int n, int[][] operations) {
        int[] arr = new int[n + 1]; // Extra space for handling 'b+1' case
        
        // Applying the operations
        for (int[] op : operations) {
            int a = op[0], b = op[1];
            arr[a] += 100;
            if (b + 1 < arr.length) {
                arr[b + 1] -= 100;
            }
        }

        // Compute prefix sum and find the maximum value
        int maxValue = 0, currentSum = 0;
        for (int i = 0; i < n; i++) {
            currentSum += arr[i];
            maxValue = Math.max(maxValue, currentSum);
        }

        return maxValue;
    }

    public static void main(String[] args) {
        int n = 5;
        int[][] operations = {
            {2, 4},
            {1, 3},
            {1, 2}
        };

        System.out.println(getMaxElement(n, operations)); // Output: 300
    }
}
