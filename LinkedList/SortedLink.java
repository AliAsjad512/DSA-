public boolean isSorted(Node head) {
    if (head == null || head.next == null) return true;

    Node temp = head;
    while (temp.next != null) {
        if (temp.data > temp.next.data) return false;
        temp = temp.next;
    }
    return true;
}
