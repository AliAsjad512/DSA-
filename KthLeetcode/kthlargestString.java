import java.util.*;

class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        PriorityQueue<String> pq = new PriorityQueue<>(
            (a, b) -> a.length() == b.length() ? a.compareTo(b) : Integer.compare(a.length(), b.length())
        );
        for (String num : nums) {
            pq.offer(num);
            if (pq.size() > k)
                pq.poll();
        }
        return pq.peek();
    }
}
