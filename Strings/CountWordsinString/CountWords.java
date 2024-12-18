package Strings.CountWordsinString;





// Count Words in String
// Difficulty: BasicAccuracy: 66.28%Submissions: 15K+Points: 1
// You are given a string s consisting of multiple words. You need to count the total words in the string. Words are separated by a single space.
// Note: It is guaranteed that the last character of the given string is not a white space.

// Examples:

// Input: s = "Geeks"
// Output: 1
// Input: s = "World is hello"
// Output: 3

public class CountWords {

    class Solution
{
    // Complete the function
    // str: input string
    public static int countWords(String str)
    {
        // find and return the number of words 
        // present in the string
        
        int count=0;
         String[] subStrings = str.split(" ");
      for(String subString: subStrings) {
         //System.out.println(subString);
         count++;
      }
      
      return count;
    }
}
    
}


class Solution
{
    // Complete the function
    // str: input string
    public static int countWords(String str)
    {
        // find and return the number of words 
        // present in the string
        int pos = str.indexOf(" ");
        int spaceCount = 1;
        
        while(pos >= 0)
        {
            pos = str.indexOf(" ", pos + 1);
            spaceCount++;
        }
        return spaceCount;
    }
}
