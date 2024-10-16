package Strings.ReverseWords;

import java.util.Scanner;

public class Reversewordsg {

    void reverseWords(char Str[], int n){
        int start=0;
        for(int end=0;end<n;end++){
            if(Str[end] == ' '){
                reverse(Str,start,end-1);
                start=end+1;
            }
        }
        reverse(Str,start,n-1);
        reverse(Str,0,n-1);

    }

    void reverse(char Str[],int low, int high){
        while(low<=high){
            //swap(Str, low, high);
            char temp;
            temp = Str[low];
            Str[low] = Str[high];
            Str[high] = temp;
            low++;
            high--;
        }

    }
    void swap(char Str[], int low, int high) {
        char temp;
        temp = Str[low];
        Str[low] = Str[high];
        Str[high] = temp;
    }
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Take the string input from the user
        System.out.println("Enter a string:");
        String input = scanner.nextLine();

        // Convert the string to a character array
        char[] charArray = input.toCharArray();

        // Create an object of Reversewordsg class and call reverseWords
        Reversewordsg rw = new Reversewordsg();
        rw.reverseWords(charArray, charArray.length);

        // Print the reversed word order
        System.out.println("Reversed words in string:");
        System.out.println(new String(charArray));

        // Close the scanner
        scanner.close();
        
    }
    
}
