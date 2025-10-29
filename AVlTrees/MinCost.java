class Solution {
    class UnionFind {
        int[] p;
        public UnionFind(int n) { p = new int[n]; for (int i = 0; i < n; i++) p[i] = i; }
        public int find(int x) { return p[x] == x ? x : (p[x] = find(p[x])); }
        public boolean union(int a, int b) {
            int pa = find(a), pb = find(b);
            if (pa == pb) return false;
            p[pa] = pb;
            return true;
        }
    }

    public int minimumCost(int n, int[][] connections) {
        Arrays.sort(connections, (a, b) -> a[2] - b[2]);
        UnionFind uf = new UnionFind(n+1);
        int cost = 0, edgesUsed = 0;
        for (int[] c : connections) {
            if (uf.union(c[0], c[1])) {
                cost += c[2];
                edgesUsed++;
                if (edgesUsed == n-1) break;
            }
        }
        return edgesUsed == n-1 ? cost : -1;
    }
}
