class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        int size = n * n;
        int[] arr = new int[size];
        
        // Flatten the 2D grid into 1D array
        int k = 0;
        for (int[] row : grid) {
            for (int val : row) {
                arr[k++] = val;
            }
        }
        
        int repeating = -1, missing = -1;

        // Step 1: Detect the repeating number (using negative marking)
        for (int i = 0; i < size; i++) {
            int index = Math.abs(arr[i]) - 1;
            if (arr[index] < 0) {
                repeating = Math.abs(arr[i]);
            } else {
                arr[index] = -arr[index];
            }
        }

        // Step 2: Detect the missing number
        for (int i = 0; i < size; i++) {
            if (arr[i] > 0) {
                missing = i + 1;
                break;
            }
        }

        return new int[]{repeating, missing};
    }
}
