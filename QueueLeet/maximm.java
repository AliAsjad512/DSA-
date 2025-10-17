import java.util.*;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || k <= 0) return new int[0];
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> dq = new LinkedList<>();
        int index = 0;

        for (int i = 0; i < n; i++) {
            // Remove out-of-window indices
            while (!dq.isEmpty() && dq.peekFirst() < i - k + 1)
                dq.pollFirst();

            // Remove smaller numbers from back
            while (!dq.isEmpty() && nums[dq.peekLast()] < nums[i])
                dq.pollLast();

            dq.offerLast(i);

            // Window starts forming after index >= k - 1
            if (i >= k - 1)
                res[index++] = nums[dq.peekFirst()];
        }
        return res;
    }
}
