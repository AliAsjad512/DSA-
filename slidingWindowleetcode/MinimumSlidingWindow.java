class Solution {
    public String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) return "";

        // Step 1: Count all characters in t
        Map<Character, Integer> tMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            tMap.put(c, tMap.getOrDefault(c, 0) + 1);
        }

        // Step 2: Sliding window pointers and helper structures
        Map<Character, Integer> windowMap = new HashMap<>();
        int have = 0, need = tMap.size();  // how many unique chars matched
        int left = 0;
        int minLen = Integer.MAX_VALUE;
        int minStart = 0;

        // Step 3: Expand window with right pointer
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            windowMap.put(c, windowMap.getOrDefault(c, 0) + 1);

            // If char in tMap and counts match, we "have" it
            if (tMap.containsKey(c) && windowMap.get(c).intValue() == tMap.get(c).intValue()) {
                have++;
            }

            // Step 4: Try to shrink window when all chars are matched
            while (have == need) {
                // Update minimum window
                if ((right - left + 1) < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }

                // Remove leftmost character
                char leftChar = s.charAt(left);
                windowMap.put(leftChar, windowMap.get(leftChar) - 1);
                if (tMap.containsKey(leftChar) && windowMap.get(leftChar) < tMap.get(leftChar)) {
                    have--;  // lost a required char
                }
                left++;
            }
        }

        // Step 5: Return result
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
        
    }
}