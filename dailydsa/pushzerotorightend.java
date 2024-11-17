package dailydsa;

public class pushzerotorightend {

class Solution {
    void pushZerosToEnd(int[] arr) {
        int n = arr.length;

        int index = 0; // Pointer for placing non-zero elements

        // Traverse the array and place non-zero elements at the `index`
        for (int i = 0; i < n; i++) {
            if (arr[i] != 0) {
                arr[index++] = arr[i];
            }
        }

        // Fill the remaining positions with zeros
        while (index < n) {
            arr[index++] = 0;
        }
 
        // code here
    }
}
    
}
