class Solution {
    public boolean canJump(int[] nums) {
        int maxReach = 0;  // farthest index we can reach

        for (int i = 0; i < nums.length; i++) {
            // If we can't reach this index, return false
            if (i > maxReach) {
                return false;
            }

            // Update the farthest we can reach from here
            maxReach = Math.max(maxReach, i + nums[i]);

            // Optional: If we can already reach or pass the last index, return true early
            if (maxReach >= nums.length - 1) {
                return true;
            }
        }

        return true;  // If loop completes, we can reach the end
    }
}
