import java.util.*;

class Solution {
    public int kthLargestSum(int[] nums, int k) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        for (int i = 1; i <= n; i++)
            prefix[i] = prefix[i - 1] + nums[i - 1];
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                int sum = prefix[end + 1] - prefix[start];
                pq.offer(sum);
                if (pq.size() > k)
                    pq.poll();
            }
        }
        return pq.peek();
    }
}
