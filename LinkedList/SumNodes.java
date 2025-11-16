class Solution {
    public int sumList(Node head) {
        int sum = 0;
        Node temp = head;

        while (temp != null) {
            sum += temp.data;
            temp = temp.next;
        }
        return sum;
    }
}
