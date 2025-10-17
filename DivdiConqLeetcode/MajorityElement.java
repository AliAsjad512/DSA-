class Solution {
    public int majorityElement(int[] nums) {
        return majority(nums, 0, nums.length - 1);
    }

    private int majority(int[] nums, int left, int right) {
        if (left == right) return nums[left];
        int mid = (left + right) / 2;
        int leftMajor = majority(nums, left, mid);
        int rightMajor = majority(nums, mid + 1, right);

        if (leftMajor == rightMajor) return leftMajor;

        int leftCount = count(nums, leftMajor, left, right);
        int rightCount = count(nums, rightMajor, left, right);
        return leftCount > rightCount ? leftMajor : rightMajor;
    }

    private int count(int[] nums, int num, int left, int right) {
        int count = 0;
        for (int i = left; i <= right; i++)
            if (nums[i] == num) count++;
        return count;
    }
}
