class Solution {
    public String decodeString(String s) {
        Stack<Integer> counts = new Stack<>();
        Stack<String> result = new Stack<>();
        String curr = "";
        int k = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                counts.push(k);
                result.push(curr);
                curr = "";
                k = 0;
            } else if (c == ']') {
                int times = counts.pop();
                StringBuilder sb = new StringBuilder(result.pop());
                for (int i = 0; i < times; i++) sb.append(curr);
                curr = sb.toString();
            } else {
                curr += c;
            }
        }

        return curr;
    }
}
