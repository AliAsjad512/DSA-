boolean search(Node root, int key) {
    if (root == null) return false;
    if (root.val == key) return true;
    if (key < root.val) return search(root.left, key);
    else return search(root.right, key);
}
