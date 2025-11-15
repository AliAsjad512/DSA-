import java.util.*;

class Solution {
    public int findMinDiff(ArrayList<Integer> arr, int m) {
        if (m == 0 || arr.size() < m) return 0;

        Collections.sort(arr);

        int minDiff = Integer.MAX_VALUE;

        for (int i = 0; i + m - 1 < arr.size(); i++) {
            int diff = arr.get(i + m - 1) - arr.get(i);
            minDiff = Math.min(minDiff, diff);
        }

        return minDiff;
    }
}
