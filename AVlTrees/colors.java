class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        final int INF = Integer.MAX_VALUE / 2;
        int[][] dist = new int[2][n];
        for (int c = 0; c < 2; c++) Arrays.fill(dist[c], INF);
        // 0 = red, 1 = blue; start from node 0 with “no previous” so we can treat both colors as valid start
        dist[0][0] = 0;
        dist[1][0] = 0;
        List<int[]>[] graph = new List[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : redEdges) graph[e[0]].add(new int[]{e[1], 0});
        for (int[] e : blueEdges) graph[e[0]].add(new int[]{e[1], 1});
        // Relax edges up to n-1 times
        for (int i = 0; i < n - 1; i++) {
            for (int u = 0; u < n; u++) {
                for (int[] nxt : graph[u]) {
                    int v = nxt[0], c = nxt[1];
                    // if current edge color c and previous color was 1-c
                    if (dist[1-c][u] + 1 < dist[c][v]) {
                        dist[c][v] = dist[1-c][u] + 1;
                    }
                }
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int d = Math.min(dist[0][i], dist[1][i]);
            ans[i] = (d >= INF ? -1 : d);
        }
        return ans;
    }
}
