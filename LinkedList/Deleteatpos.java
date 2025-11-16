public Node deleteAtPosition(Node head, int pos) {
    if (pos == 1) return head.next;

    Node temp = head;
    for (int i = 1; i < pos - 1 && temp != null; i++) {
        temp = temp.next;
    }

    if (temp == null || temp.next == null) return head;

    temp.next = temp.next.next;
    return head;
}
