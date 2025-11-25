import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();        // number of queries
        
        int maxSize = 100000;
        int[] stack = new int[maxSize];
        int top = -1;                // top pointer
        
        while (q-- > 0) {
            int type = sc.nextInt();
            
            if (type == 1) {                   // Push x
                int x = sc.nextInt();
                if (top + 1 == maxSize) {
                    System.out.println("Stack Full");
                } else {
                    stack[++top] = x;
                }
            } 
            else if (type == 2) {              // Pop
                if (top == -1) {
                    System.out.println("Stack Empty");
                } else {
                    top--;
                }
            } 
            else if (type == 3) {              // Display
                if (top == -1) {
                    System.out.println("-1");
                } else {
                    for (int i = 0; i <= top; i++) {
                        System.out.print(stack[i] + " ");
                    }
                    System.out.println();
                }
            }
        }
        sc.close();
    }
}
