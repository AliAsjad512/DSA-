class Solution {
    public void sortBinaryArray(int[] arr) {
        int left = 0, right = arr.length - 1;

        while (left < right) {
            while (arr[left] == 0 && left < right) left++;
            while (arr[right] == 1 && left < right) right--;

            if (left < right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
    }
}
