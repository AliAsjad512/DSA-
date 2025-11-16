public Node removeDuplicates(Node head) {
    if (head == null) return null;

    Node temp = head;
    while (temp != null && temp.next != null) {
        if (temp.data == temp.next.data) {
            temp.next = temp.next.next;
        } else {
            temp = temp.next;
        }
    }
    return head;
}
