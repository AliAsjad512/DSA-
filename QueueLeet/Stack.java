import java.util.LinkedList;
import java.util.Queue;

class MyStack {
    Queue<Integer> q = new LinkedList<>();

    public void push(int x) {
        q.add(x);
        int size = q.size();
        while (size > 1) {
            q.add(q.remove());
            size--;
        }
    }

    public int pop() {
        return q.remove();
    }

    public int top() {
        return q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}
