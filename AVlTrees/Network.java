class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        final int INF = Integer.MAX_VALUE / 2;
        int[] dist = new int[N+1];
        Arrays.fill(dist, INF);
        dist[K] = 0;
        // Relax edges N-1 times
        for (int i = 1; i <= N-1; i++) {
            boolean updated = false;
            for (int[] e : times) {
                int u = e[0], v = e[1], w = e[2];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    updated = true;
                }
            }
            if (!updated) break;
        }
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            if (dist[i] == INF) return -1;
            ans = Math.max(ans, dist[i]);
        }
        return ans;
    }
}
