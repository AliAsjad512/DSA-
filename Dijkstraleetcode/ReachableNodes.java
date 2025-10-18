import java.util.*;

public class ReachableNodes {
    public int reachableNodes(int[][] edges, int maxMoves, int n) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.computeIfAbsent(e[0], x -> new ArrayList<>()).add(new int[]{e[1], e[2]});
            graph.computeIfAbsent(e[1], x -> new ArrayList<>()).add(new int[]{e[0], e[2]});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{0, 0});

        Map<Long, Integer> used = new HashMap<>();
        int ans = 0;

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0], d = curr[1];
            if (d > dist[node]) continue;
            ans++;

            if (graph.containsKey(node)) {
                for (int[] e : graph.get(node)) {
                    int nei = e[0], cnt = e[1];
                    long key = (long) node * n + nei;
                    int remain = maxMoves - d;
                    used.put(key, Math.min(cnt, remain));

                    int newDist = d + cnt + 1;
                    if (newDist < dist[nei] && newDist <= maxMoves) {
                        dist[nei] = newDist;
                        pq.offer(new int[]{nei, newDist});
                    }
                }
            }
        }

        for (int[] e : edges) {
            int u = e[0], v = e[1], cnt = e[2];
            long uv = (long) u * n + v, vu = (long) v * n + u;
            ans += Math.min(cnt, used.getOrDefault(uv, 0) + used.getOrDefault(vu, 0));
        }

        return ans;
    }
}
