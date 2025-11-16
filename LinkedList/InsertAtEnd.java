class Solution {
    public Node insertEnd(Node head, int val) {
        Node newNode = new Node(val);

        if (head == null) return newNode;

        Node temp = head;
        while (temp.next != null) temp = temp.next;

        temp.next = newNode;
        return head;
    }
}
