public Node kthFromEnd(Node head, int k) {
    Node fast = head, slow = head;

    // Move fast k steps
    for (int i = 0; i < k; i++) {
        if (fast == null) return null; // K > length
        fast = fast.next;
    }

    // Move both until fast reaches end
    while (fast != null) {
        fast = fast.next;
        slow = slow.next;
    }

    return slow;
}
