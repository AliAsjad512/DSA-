class Solution {
    public int maxSubArray(int[] nums) {
        return helper(nums, 0, nums.length - 1);
    }

    private int helper(int[] nums, int left, int right) {
        if (left == right) return nums[left];
        int mid = (left + right) / 2;
        int leftSum = helper(nums, left, mid);
        int rightSum = helper(nums, mid + 1, right);
        int crossSum = cross(nums, left, right, mid);
        return Math.max(Math.max(leftSum, rightSum), crossSum);
    }

    private int cross(int[] nums, int left, int right, int mid) {
        int leftSum = Integer.MIN_VALUE, rightSum = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = mid; i >= left; i--) {
            sum += nums[i];
            leftSum = Math.max(leftSum, sum);
        }
        sum = 0;
        for (int i = mid + 1; i <= right; i++) {
            sum += nums[i];
            rightSum = Math.max(rightSum, sum);
        }
        return leftSum + rightSum;
    }
}
