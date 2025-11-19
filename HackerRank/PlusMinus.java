import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int pos = 0, neg = 0, zero = 0;

        for(int i = 0; i < n; i++){
            int x = sc.nextInt();
            if(x > 0) pos++;
            else if(x < 0) neg++;
            else zero++;
        }

        System.out.printf("%.6f%n", (double)pos / n);
        System.out.printf("%.6f%n", (double)neg / n);
        System.out.printf("%.6f%n", (double)zero / n);
    }
}
