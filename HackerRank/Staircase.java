import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int s = 0; s < n - i; s++)
                System.out.print(" ");
            for (int h = 0; h < i; h++)
                System.out.print("#");
            System.out.println();
        }
    }
}
