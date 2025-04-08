//APPROACH-1
class Solution {
    public:
        bool isSubsequence(string s, string t) {
            
            int tpos=0;
            for(int i=0;s[i]!='\0';++i)
            {
                while(t[tpos] && t[tpos]!=s[i])
                    tpos+=1;
                if(t[tpos]=='\0')
                    return false;
                tpos+=1;
            }
            return true;
        }
    };


    import java.util.*;

public class Solution {
    public boolean isSubsequence(String s, String t) {
        Map<Character, List<Integer>> map = new HashMap<>();

        // Build a map of character to list of indices in 't'
        for (int i = 0; i < t.length(); ++i) {
            char c = t.charAt(i);
            map.computeIfAbsent(c, k -> new ArrayList<>()).add(i);
        }

        int low = -1; // Previous index found
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);

            if (!map.containsKey(c)) return false;

            List<Integer> indices = map.get(c);

            // Find the smallest index > low using binary search
            int pos = upperBound(indices, low);
            if (pos == indices.size()) return false;

            low = indices.get(pos);
        }

        return true;
    }

    // Custom upperBound (similar to C++ std::upper_bound)
    private int upperBound(List<Integer> list, int target) {
        int left = 0, right = list.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list.get(mid) <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left; // First index with value > target
    }

    // You can add a main method to test this:
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isSubsequence("abc", "ahbgdc")); // true
        System.out.println(sol.isSubsequence("axc", "ahbgdc")); // false
    }
}

