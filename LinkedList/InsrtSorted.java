class Solution {
    public Node insertSorted(Node head, int val) {
        Node newNode = new Node(val);

        if (head == null || head.data >= val) {
            newNode.next = head;
            return newNode;
        }

        Node temp = head;
        while (temp.next != null && temp.next.data < val) {
            temp = temp.next;
        }

        newNode.next = temp.next;
        temp.next = newNode;

        return head;
    }
}
