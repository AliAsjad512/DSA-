package Strings.LexicographicRank;

public record LexicographicRank() {
    void permute(char[] chars, int idx) {
        if (idx == chars.length) {
            System.out.println(new String(chars));
            return;
        }
        
        for (int i = idx; i < chars.length; i++) {
            // Swap chars[i] with chars[idx]
            char temp = chars[i];
            chars[i] = chars[idx];
            chars[idx] = temp;

            // Recursive call with the updated array
            permute(chars, idx + 1);

            // Backtrack to restore original order
            temp = chars[i];
            chars[i] = chars[idx];
            chars[idx] = temp;
        }
    }
    public static void main(String[] args) {
        LexicographicRank b = new LexicographicRank();
        String s = "bac";
        b.permute(s.toCharArray(), 0); // Pass the array directly
        
    }
}
