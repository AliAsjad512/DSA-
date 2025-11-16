class Solution {
    public Node joinLists(Node head1, Node head2) {
        if (head1 == null) return head2;
        if (head2 == null) return head1;

        Node temp = head1;
        while (temp.next != null) temp = temp.next;

        temp.next = head2;
        return head1;
    }
}
