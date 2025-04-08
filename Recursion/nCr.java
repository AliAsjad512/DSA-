// You are given two numbers n and r. You need to find nCr.
// nCr = (n!) / ((n-r)!*(r!))
// In recursive way, we can write nCr as nCr = (n-1)C(r-1) + (n-1)Cr

// Example 1:

// Input:
// n = 5, r = 2
// Output: 10
// Example 2:

// Input:
// n = 4, r = 1
// Output: 4


nCr(5,2)
├── nCr(4,1)
│   ├── nCr(3,0) → 1   ← base case
│   └── nCr(3,1)
│       ├── nCr(2,0) → 1
│       └── nCr(2,1)
│           ├── nCr(1,0) → 1
│           └── nCr(1,1) → 1
│       → nCr(2,1) = 1 + 1 = 2
│   → nCr(3,1) = 1 + 2 = 3
│ → nCr(4,1) = 1 + 3 = 4
│
└── nCr(4,2)
    ├── nCr(3,1)
    │   (already calculated above → 3)
    └── nCr(3,2)
        ├── nCr(2,1)
        │   (already calculated above → 2)
        └── nCr(2,2) → 1   ← base case
    → nCr(3,2) = 2 + 1 = 3
→ nCr(4,2) = 3 + 3 = 6


class Get
{
    public static int nCr(int n,int r)
    {
        // your code here
        if(r==0 || r==n){
            return 1;
        }
        return nCr(n-1,r-1)+nCr(n-1,r);
    }
}