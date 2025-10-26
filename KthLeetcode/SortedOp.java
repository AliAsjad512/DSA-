import java.util.*;

class Solution {
    public int kthLargest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> b[0] - a[0]
        );
        for (int i = 0; i < n; i++)
            pq.offer(new int[]{matrix[i][n - 1], i, n - 1});
        
        int val = 0;
        while (k-- > 0) {
            int[] cur = pq.poll();
            val = cur[0];
            int r = cur[1], c = cur[2];
            if (c - 1 >= 0)
                pq.offer(new int[]{matrix[r][c - 1], r, c - 1});
        }
        return val;
    }
}
