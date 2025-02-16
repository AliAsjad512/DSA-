//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class Driver {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(read.readLine());
            String str[] = read.readLine().trim().split(" ");

            int input[] = new int[n];
            for (int i = 0; i < n; i++) {
                input[i] = Integer.parseInt(str[i]);
            }

            // int x = Integer.parseInt(read.readLine());
            Get obj = new Get();
            obj.reverseArray(input, n);

            for (int i = 0; i < n; i++) System.out.print(input[i] + " ");

            System.out.println();
        
System.out.println("~");
}
    }
}

// } Driver Code Ends


// User function Template for Java

class Get {
    public static void reverseArray(int arr[], int n) {
        
        int i=0;
        int p2=arr.length-1;
        int temp=0;
        // Your code here
        while(i<(n/2)){
            temp=arr[i];
            arr[i] = arr[p2];
            arr[p2] = temp;
            p2--;
            i++;
            
        }
        
    }
}
