package dailydsa;

public class permutation {

    public static void generatePermutations(int arr[], int l, int r) {
        // Base case: if l == r, print the permutation
        if (l == r) {
            // Print the current permutation
            for (int i = 0; i < arr.length; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println(); // Move to the next line after printing one permutation
        } else {
            // Generate permutations by swapping each element
            for (int i = l; i <= r; i++) {
                // Swap the elements at position l and i
                swap(arr, l, i);
                // Recur for the next position
                generatePermutations(arr, l + 1, r);
                // Backtrack to the previous state by swapping the elements back
                swap(arr, l, i);
            }
        }
    }

    // Method to swap elements in the integer array
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int arr[] = {1, 2, 3}; // Example integer array input
        int n = arr.length;
        generatePermutations(arr, 0, n - 1); // Generate all permutations
    }
    
}
