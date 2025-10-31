class Codec {
    public String serialize(TreeNode root) {
        if (root == null) return "X,";
        return root.val + "," + serialize(root.left) + serialize(root.right);
    }

    public TreeNode deserialize(String data) {
        Queue<String> nodes = new LinkedList<>(Arrays.asList(data.split(",")));
        return build(nodes);
    }

    private TreeNode build(Queue<String> nodes) {
        String val = nodes.poll();
        if (val.equals("X")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(val));
        root.left = build(nodes);
        root.right = build(nodes);
        return root;
    }
}
