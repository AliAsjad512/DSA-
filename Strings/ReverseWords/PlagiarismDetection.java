package Strings.ReverseWords;
import java.util.ArrayList;
import java.util.List;

public class PlagiarismDetection {
    public final static int d = 256;

static List<Integer> searchPattern( String txt, String pat, int q){

    int m=pat.length();
    int n=txt.length();
    int i,j;
    int p=0;
    int t=0;
    int h=1;
    List<Integer> foundIndexes = new ArrayList<>();
    for (i = 0; i < m - 1; i++) {
        h = (h * d) % q;
    }

    for (i = 0; i < m; i++) {
        p = (p * d + pat.charAt(i)) % q;
        t = (t * d + txt.charAt(i)) % q;
    }
    for (i = 0; i <= n - m; i++) {
        // Check the hash values of current window of text and pattern
        if (p == t) {
            // Check characters one by one if hash matches
            for (j = 0; j < m; j++) {
                if (txt.charAt(i + j) != pat.charAt(j)) {
                    break;
                }
            }
            // If p == t and pat[0...m-1] = txt[i...i+m-1], it is a match
            if (j == m) {
                foundIndexes.add(i);
            }
        }
        // Calculate the hash value for next window of text
        if (i < n - m) {
            t = (d * (t - txt.charAt(i) * h) + txt.charAt(i + m)) % q;
            // Convert negative hash value to positive
            if (t < 0) {
                t = t + q;
            }
        }
    }
    return foundIndexes;



}



//Fucntion to check plagiarims by comparing phrases from source in the target text
    static void checkPlagiarism(String sourceDoc, String targetDoc, int phraseLength, int prime){
        //Split the source document into phrases of the given length
   for(int i=0;i<=sourceDoc.length()-phraseLength;i++){
    String phrase= sourceDoc.substring(i, i+phraseLength);
  List<Integer> foundAt = searchPattern(targetDoc,phrase,prime);
  if (!foundAt.isEmpty()) {
    System.out.println("Phrase '" + phrase + "' found at positions: " + foundAt);
}

   }






    }

    public static void main(String[] args) {
        
   String sourceDoc="This is a sample document used for plagiarism detection";

   String targetDoc="we will use this document to detect plagiarims in a sample text";

   int phraseLength=6;

   int prime=101;
   checkPlagiarism(sourceDoc,targetDoc,phraseLength,prime);






    }
    
}
