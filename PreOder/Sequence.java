class Solution {
    public boolean verifyPreorder(int[] preorder) {
        Stack<Integer> stack = new Stack<>();
        int lowerBound = Integer.MIN_VALUE;

        for (int val : preorder) {
            if (val < lowerBound) return false;
            while (!stack.isEmpty() && val > stack.peek())
                lowerBound = stack.pop();
            stack.push(val);
        }
        return true;
    }
}
