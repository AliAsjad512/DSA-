import java.util.*;

class Node {
    public int val;
    public List<Node> children;
    public Node() {}
    public Node(int val) { this.val = val; }
}

class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> result = new ArrayList<>();
        helper(root, result);
        return result;
    }

    private void helper(Node node, List<Integer> result) {
        if (node == null) return;
        for (Node child : node.children) {
            helper(child, result);
        }
        result.add(node.val);
    }
}
