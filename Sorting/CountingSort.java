class CountingSort {
    public void countSort(int[] arr) {
        int max = 0;
        for (int x : arr) max = Math.max(max, x);

        int[] count = new int[max + 1];

        for (int x : arr) count[x]++;

        int idx = 0;
        for (int i = 0; i <= max; i++) {
            while (count[i]-- > 0) {
                arr[idx++] = i;
            }
        }
    }
}
