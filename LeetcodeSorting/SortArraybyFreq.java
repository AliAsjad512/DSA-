import java.util.*;
class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) freq.put(n, freq.getOrDefault(n, 0) + 1);

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = 0; j < nums.length - 1 - i; j++) {
                int a = nums[j], b = nums[j + 1];
                if (freq.get(a) > freq.get(b) || 
                   (freq.get(a).equals(freq.get(b)) && a < b)) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
        return nums;
    }
}
