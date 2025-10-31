class Solution {
    int preIndex = 0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> inMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++)
            inMap.put(inorder[i], i);
        return build(preorder, 0, inorder.length - 1, inMap);
    }

    private TreeNode build(int[] preorder, int inStart, int inEnd, Map<Integer, Integer> inMap) {
        if (inStart > inEnd) return null;
        TreeNode root = new TreeNode(preorder[preIndex++]);
        int inIndex = inMap.get(root.val);
        root.left = build(preorder, inStart, inIndex - 1, inMap);
        root.right = build(preorder, inIndex + 1, inEnd, inMap);
        return root;
    }
}
