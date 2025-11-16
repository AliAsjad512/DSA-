class Solution {
    public Node insertInMiddle(Node head, int val) {
        Node newNode = new Node(val);

        if (head == null) return newNode;

        Node slow = head, fast = head;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        newNode.next = slow.next;
        slow.next = newNode;

        return head;
    }
}
