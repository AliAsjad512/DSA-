import java.util.*;

class Solution {
    public int kthLargest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int[] row : matrix)
            for (int val : row)
                maxHeap.offer(val);
        for (int i = 1; i < k; i++)
            maxHeap.poll();
        return maxHeap.peek();
    }
}
