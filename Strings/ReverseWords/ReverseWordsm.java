package Strings.ReverseWords;

public class ReverseWordsm {

      public static void main(String[] args) {
        
      
    String sentence = "How are you";
        StringBuilder word = new StringBuilder();

        // Use a dynamic array to store words
        String[] words = new String[sentence.length()]; // Allocate max possible words
        int wordCount = 0; // Keep track of the number of words

        // Iterate through the characters in the string
        for (int i = 0; i < sentence.length(); i++) {
            char ch = sentence.charAt(i);
            
            // Check if the character is a space
            if (ch == ' ') {
                if (word.length() > 0) { // Only push non-empty words
                    words[wordCount++] = word.toString(); // Add word to array
                    word.setLength(0); // Reset for the next word
                }
            } else {
                word.append(ch); // Build the current word
            }
        }
        
        // Add the last word if there is one
        if (word.length() > 0) {
            words[wordCount++] = word.toString();
        }

        // Now, reverse the words and build the new reversed sentence
        StringBuilder reversedSentence = new StringBuilder();
        for (int i = wordCount - 1; i >= 0; i--) {
            reversedSentence.append(words[i]); // Append words in reverse order
            if (i > 0) {
                reversedSentence.append(" "); // Add space between words
            }
        }

        // Print the reversed sentence
        System.out.println("Reversed Sentence: " + reversedSentence.toString());
    }
    
}

