import java.util.*;

class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.length;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Double.compare((double) arr[a[0]] / arr[a[1]], (double) arr[b[0]] / arr[b[1]])
        );
        for (int i = 0; i < n - 1; i++)
            pq.offer(new int[]{i, n - 1});
        
        while (--k > 0) {
            int[] cur = pq.poll();
            if (cur[1] - 1 > cur[0])
                pq.offer(new int[]{cur[0], cur[1] - 1});
        }
        int[] res = pq.peek();
        return new int[]{arr[res[0]], arr[res[1]]};
    }
}
