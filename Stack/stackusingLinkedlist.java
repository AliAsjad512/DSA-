class Node {
    int data;
    Node next;
    
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Stack {
    private Node top;
    private int size;

    public Stack() {
        top = null;
        size = 0;
    }

    // (i) push(x): Insert element at top
    public void push(int x) {
        Node newNode = new Node(x);
        newNode.next = top;
        top = newNode;
        size++;
    }

    // (ii) pop(): Remove top element
    public void pop() {
        if (top != null) {
            top = top.next;
            size--;
        }
    }

    // (iii) peek(): Return top element, else -1
    public int peek() {
        if (top == null) return -1;
        return top.data;
    }

    // (iv) isEmpty(): return true if empty else false
    public boolean isEmpty() {
        return top == null;
    }

    // (v) size(): Return number of elements in stack
    public int size() {
        return size;
    }
}
