// 





static int RecursivePower(int n, int p) {
    if (p == 0) {
        return 1;
    }
    return n * RecursivePower(n, p - 1);
}






// RecursivePower(2, 0) = 1
// RecursivePower(2, 1) = 2 * 1 = 2
// RecursivePower(2, 2) = 2 * 2 = 4
// RecursivePower(2, 3) = 2 * 4 = 8 ✅