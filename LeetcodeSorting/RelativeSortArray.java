import java.util.*;
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> order = new HashMap<>();
        for (int i = 0; i < arr2.length; i++) order.put(arr2[i], i);

        // Bubble sort using custom order
        for (int i = 0; i < arr1.length - 1; i++) {
            for (int j = 0; j < arr1.length - 1 - i; j++) {
                int a = arr1[j], b = arr1[j + 1];
                if (compare(a, b, order) > 0) {
                    int temp = arr1[j];
                    arr1[j] = arr1[j + 1];
                    arr1[j + 1] = temp;
                }
            }
        }
        return arr1;
    }

    private int compare(int a, int b, Map<Integer, Integer> order) {
        if (order.containsKey(a) && order.containsKey(b))
            return order.get(a) - order.get(b);
        if (order.containsKey(a)) return -1;
        if (order.containsKey(b)) return 1;
        return a - b;
    }
}
