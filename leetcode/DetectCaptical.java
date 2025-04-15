class Solution {
    public boolean detectCapitalUse(String word) {
        int n = word.length();
        int upper = 0;

        for (int i = 0; i < n; i++) {
            if (Character.isUpperCase(word.charAt(i))) {
                upper++;
            }
        }

        if (upper == n || upper == 0 || (Character.isUpperCase(word.charAt(0)) && upper == 1)) {
            return true;
        }

        return false;
    }
}


class Solution {
    private boolean isLower(char c) {
        return c >= 'a' && c <= 'z';
    }

    private boolean isUpper(char c) {
        return c >= 'A' && c <= 'Z';
    }

    public boolean detectCapitalUse(String word) {
        int n = word.length();
        int i;

        // If 1st character is lowercase
        if (isLower(word.charAt(0))) {
            i = 1;
            while (i < n && isLower(word.charAt(i))) {
                i++;
            }
            return i == n;
        } else {
            // If all characters are uppercase
            i = 1;
            while (i < n && isUpper(word.charAt(i))) {
                i++;
            }
            if (i == n) {
                return true;
            } else if (i > 1) {
                return false;
            }

            // If all characters from 2nd are lowercase
            while (i < n && isLower(word.charAt(i))) {
                i++;
            }
            return i == n;
        }
    }
}
