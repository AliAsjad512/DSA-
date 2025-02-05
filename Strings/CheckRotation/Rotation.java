package CheckRotation;


import java.util.Arrays;

class Main {
    public static String shiftRight(String s2) {
        char[] letters = s2.toCharArray();

        char last = letters[letters.length - 1]; // save off last element

        // shift right
        for (int index = letters.length - 2; index >= 0; index--) {
            letters[index + 1] = letters[index];
        }

        // wrap last element into first slot
        letters[0] = last;
        return new String(letters); // return the shifted string
    }

    public static void main(String[] args) {
        String s = "abcd";
        String s2 = "cdab";

        String k = shiftRight(s2);
        boolean matchFound = false;

        // Check if s equals k after any number of shifts
        for (int i = 0; i < s.length(); i++) {
            if (s.equals(k)) {
                matchFound = true;
                System.out.println("Yes");
                break;
            }
            k = shiftRight(k); // Shift k for the next iteration
        }

        if (!matchFound) {
            System.out.println("No"); // Print "No" if no match is found
        }
    }
}
