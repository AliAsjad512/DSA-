import java.util.*;

public class CheapestFlights {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] f : flights) {
            graph.computeIfAbsent(f[0], x -> new ArrayList<>()).add(new int[]{f[1], f[2]});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{src, 0, 0}); // [node, cost, stops]

        int[] bestStops = new int[n];
        Arrays.fill(bestStops, Integer.MAX_VALUE);

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0], cost = curr[1], stops = curr[2];

            if (node == dst) return cost;
            if (stops > K || stops > bestStops[node]) continue;

            bestStops[node] = stops;

            if (graph.containsKey(node)) {
                for (int[] next : graph.get(node)) {
                    pq.offer(new int[]{next[0], cost + next[1], stops + 1});
                }
            }
        }
        return -1;
    }
}
