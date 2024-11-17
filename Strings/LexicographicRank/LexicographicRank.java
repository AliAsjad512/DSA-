package Strings.LexicographicRank;
import java.util.Arrays;
public record LexicographicRank() {
    
    void permute(char[] chars, int idx) {
        String s;
        
        if (idx == chars.length) {
            s=new String(chars);
            System.out.println(s);
            
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
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        b.permute(chars, 0); // Pass the array directly
        
    }
}
