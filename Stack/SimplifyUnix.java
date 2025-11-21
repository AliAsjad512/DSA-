class Solution {
    public String simplifyPath(String path) {
        Stack<String> st = new Stack<>();
        String[] parts = path.split("/");

        for (String p : parts) {
            if (p.equals("") || p.equals(".")) continue;
            else if (p.equals("..")) {
                if (!st.isEmpty()) st.pop();
            } else {
                st.push(p);
            }
        }

        StringBuilder sb = new StringBuilder("/");
        for (int i = 0; i < st.size(); i++) {
            sb.append(st.get(i));
            if (i < st.size() - 1) sb.append("/");
        }

        return sb.toString();
    }
}
