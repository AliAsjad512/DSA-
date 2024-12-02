package Strings.Areangrama;

public class Areangram {

    // Function to compare two character frequency arrays
    public static boolean areSame(int[] CP, int[] CT) {
        // Compare both arrays element by element
        for (int i = 0; i < 256; i++) {
            if (CP[i] != CT[i]) {
                return false; // If any character's count doesn't match, return false
            }
        }
        return true; // If all character counts match, return true
    }

    // Function to check if an anagram of 'pat' is present in 'txt'
    public static boolean isPresent(String txt, String pat) {
        // Array to store the frequency of characters in 'txt' and 'pat'
        int[] CT = new int[256];  // Frequency count of characters in the current window of 'txt'
        int[] CP = new int[256];  // Frequency count of characters in 'pat'

        // Edge case: if 'pat' is longer than 'txt', return false
        if (pat.length() > txt.length()) {
            return false;
        }

        // Initialize frequency arrays for 'txt' and 'pat'
        for (int i = 0; i < pat.length(); i++) {
            CT[txt.charAt(i)]++;   // Frequency of characters in 'txt' (sliding window)
            CP[pat.charAt(i)]++;   // Frequency of characters in 'pat'
        }

        // Sliding window approach
        for (int i = pat.length(); i < txt.length(); i++) {
            // If the frequencies match, then 'pat' is an anagram of the current window
            if (areSame(CP, CT)) {
                return true;
            }

            // Update the frequency of the current window in 'txt'
            CT[txt.charAt(i)]++;             // Add the new character from 'txt' into the window
            CT[txt.charAt(i - pat.length())]--; // Remove the old character that just left the window
        }

        // Check for the last window
        return areSame(CP, CT);
    }

    // Main function to test the isPresent function
    public static void main(String[] args) {
        String txt = "oidbcaf";
        String pat = "abc";

        if (isPresent(txt, pat)) {
            System.out.println("Anagram of " + pat + " is present in " + txt);
        } else {
            System.out.println("Anagram of " + pat + " is NOT present in " + txt);
        }
    }
}
