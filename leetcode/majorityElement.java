class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        int majority = nums[0];
        int count = 1;

        for (int i = 1; i < n; i++) {
            if (nums[i] == majority) {
                count++;
            } else {
                count--;
                if (count == 0) {
                    majority = nums[i];
                    count = 1;
                }
            }
        }

        return majority;
    }
}


//This solution uses the Boyer-Moore Majority Vote Algorithm to find the majority element in an array, which is the element that appears more than n / 2 times. The algorithm maintains a candidate for the majority element and a counter. It starts by assuming the first element is the majority and sets the count to 1. Then, for each next element, if it matches the current candidate, the count is increased. If it doesn’t match, the count is decreased. When the count reaches zero, the candidate is replaced with the current element and the count is reset to 1. For example, in the array [2, 2, 1, 1, 1, 2, 2], the algorithm starts with 2 as the majority. It increases and decreases the count as it loops through the array, and by the end, the majority element remains 2. This approach is efficient and works in linear time with constant space.