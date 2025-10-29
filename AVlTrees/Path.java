class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        double[] prob = new double[n];
        prob[start] = 1.0;
        for (int i = 0; i < n-1; i++) {
            boolean updated = false;
            for (int j = 0; j < edges.length; j++) {
                int u = edges[j][0], v = edges[j][1];
                double p = succProb[j];
                if (prob[u] * p > prob[v]) {
                    prob[v] = prob[u] * p;
                    updated = true;
                }
                if (prob[v] * p > prob[u]) {
                    prob[u] = prob[v] * p;
                    updated = true;
                }
            }
            if (!updated) break;
        }
        return prob[end];
    }
}
