class Solution {
    public int characterReplacement(String s, int k) {
        

int p1 = 0; 
        int maxCount = 0; 
        int maxLength = 0; 
        
        Map<Character, Integer> freq = new HashMap<>();
        
        for (int p2 = 0; p2 < s.length(); p2++) {
            char c = s.charAt(p2);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
            
            
            maxCount = Math.max(maxCount, freq.get(c));
            
            
            while ((p2 - p1 + 1) - maxCount > k) {
                char leftChar = s.charAt(p1);
                freq.put(leftChar, freq.get(leftChar) - 1);
                p1++;
            }
            
            
            maxLength = Math.max(maxLength, p2 - p1 + 1);
        }

       return maxLength;





        
    }
}