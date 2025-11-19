import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = new int[3];
        int[] b = new int[3];

        for (int i = 0; i < 3; i++) a[i] = sc.nextInt();
        for (int i = 0; i < 3; i++) b[i] = sc.nextInt();

        int aScore = 0, bScore = 0;

        for (int i = 0; i < 3; i++) {
            if (a[i] > b[i]) aScore++;
            else if (b[i] > a[i]) bScore++;
        }

        System.out.println(aScore + " " + bScore);
    }
}
