class Main {
    
    public static int[] computelps(String s) {
        int lps[] = new int[s.length()];
        lps[0] = 0;
        int i = 1;
        int n = lps.length;
        int len = 0;

        while (i < n) {
            if (s.charAt(i) == s.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    public static void main(String[] args) {
        String s1 = "abcd";
        String s2 = "cdab";
        String s3 = s1 + s1; // "abcdabcd"
        int text = s3.length();
        int pat = s2.length();
        
        int lps[] = computelps(s2);

        int i = 0;
        int j = 0;
        
        while (i < text) {
            if (s3.charAt(i) == s2.charAt(j)) {
                i++;
                j++;
            }
            if (j == pat) {
                System.out.println("index " + ((i - j) + 1));  // Print index of occurrence
                j = lps[j - 1];  // Continue searching instead of breaking
            } else if (i < text && s3.charAt(i) != s2.charAt(j)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
    }
}
