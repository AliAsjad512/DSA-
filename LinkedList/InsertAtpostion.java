class Solution {
    public Node insertAtPosition(Node head, int pos, int val) {
        Node newNode = new Node(val);

        if (pos == 1) {
            newNode.next = head;
            return newNode;
        }

        Node temp = head;
        for (int i = 1; i < pos - 1 && temp != null; i++) {
            temp = temp.next;
        }

        if (temp == null) return head; // invalid pos

        newNode.next = temp.next;
        temp.next = newNode;

        return head;
    }
}
