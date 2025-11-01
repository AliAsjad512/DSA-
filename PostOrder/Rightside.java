class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        rightView(root, result, 0);
        return result;
    }

    private void rightView(TreeNode node, List<Integer> result, int level) {
        if (node == null) return;
        if (level == result.size()) result.add(node.val);
        rightView(node.right, result, level + 1); // right first
        rightView(node.left, result, level + 1);
    }
}
