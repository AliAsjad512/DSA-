package dailydsa;


// Next Permutation
// Difficulty: MediumAccuracy: 40.66%Submissions: 169K+Points: 4
// Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

// Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

// Examples:

// Input: arr = [2, 4, 1, 7, 5, 0]
// Output: [2, 4, 5, 0, 1, 7]
// Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
// Input: arr = [3, 2, 1]
// Output: [1, 2, 3]
// Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
// Input: arr = [3, 4, 2, 5, 1]
// Output: [3, 4, 5, 1, 2]
// Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.






//First of  find the largest i such that arr[i] < arr[i+1]
//loop through all elements to find 
// if no such elements exist return the lowest possible permuataion by sorting the array
// Find largest j such that arr[x] < arr[j] 
// loop through largesstx to n
// swap elements
//reverse the elemennts 


// Find the largest index largestx such that arr[largestx] < arr[largestx + 1].
// Find the largest index largestY such that arr[largestY] > arr[largestx].
// Swap arr[largestx] and arr[largestY].
// Reverse the subarray from index largestx + 1 to the end of the array.

public class nextpermutation {

    
        public static void swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        
        // Reverse the part of the array from index 'i' to 'j'
        public static void reverse(int[] arr, int i, int j) {
            while (i < j) {
                swap(arr, i, j);
                i++;
                j--;
            }
        }
       public static void nextPermutation(int[] arr) {
           
           int n = arr.length;
           
           // Find the largest index 'largestx' such that a[largestx] < a[largestx + 1]
           int largestx = -1;
           for (int i = 0; i < n - 1; i++) {
               if (arr[i] < arr[i + 1]) {
                   largestx = i;
               }
           }
           
           // If no such index exists, the array is in the largest permutation
           if (largestx == -1) {
               // Return the smallest permutation (sorted array)
               java.util.Arrays.sort(arr);  // Sort the array in ascending order
            //   System.out.println("Smallest permutation: ");
            //   for (int i = 0; i < a.length; i++) {
            //       System.out.print(a[i] + " ");
            //   }
               return;
           }
           
           // Find the largest index 'largestY' such that a[largestY] > a[largestx]
           int largestY = -1;
           for (int j = largestx + 1; j < n; j++) {
               if (arr[j] > arr[largestx]) {
                   largestY = j;
               }
           }
           
           // Swap the elements at largestx and largestY
           swap(arr, largestx, largestY);
           
           // Reverse the portion of the array after 'largestx'
           reverse(arr, largestx + 1, n - 1);
            // code here
        }
        
        
        
        
    
    
    }
    

