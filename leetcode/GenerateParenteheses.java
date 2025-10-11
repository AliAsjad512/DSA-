import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        generate(res, "", 0, 0, n);
        return res;
    }

    private void generate(List<String> res, String current, int open, int close, int n) {
        if (current.length() == n * 2) {
            res.add(current);
            return;
        }
        if (open < n) generate(res, current + "(", open + 1, close, n);
        if (close < open) generate(res, current + ")", open, close + 1, n);
    }
}
