import java.util.*;

void levelOrder(Node root) {
    if (root == null) return;

    Queue<Node> q = new LinkedList<>();
    q.add(root);

    while (!q.isEmpty()) {
        Node curr = q.poll();
        System.out.print(curr.val + " ");

        if (curr.left != null) q.add(curr.left);
        if (curr.right != null) q.add(curr.right);
    }
}
