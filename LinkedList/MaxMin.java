class Solution {
    public int maxValue(Node head) {
        int max = Integer.MIN_VALUE;
        Node temp = head;

        while (temp != null) {
            max = Math.max(max, temp.data);
            temp = temp.next;
        }
        return max;
    }

    public int minValue(Node head) {
        int min = Integer.MAX_VALUE;
        Node temp = head;

        while (temp != null) {
            min = Math.min(min, temp.data);
            temp = temp.next;
        }
        return min;
    }
}
