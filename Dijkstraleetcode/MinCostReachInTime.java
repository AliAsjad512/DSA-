import java.util.*;

public class MinCostReachInTime {
    public int minCost(int maxTime, int[][] edges, int[] passingFees) {
        int n = passingFees.length;
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.computeIfAbsent(e[0], x -> new ArrayList<>()).add(new int[]{e[1], e[2]});
            graph.computeIfAbsent(e[1], x -> new ArrayList<>()).add(new int[]{e[0], e[2]});
        }

        int[][] cost = new int[n][maxTime + 1];
        for (int[] c : cost) Arrays.fill(c, Integer.MAX_VALUE);
        cost[0][0] = passingFees[0];

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{0, passingFees[0], 0}); // [node, totalCost, time]

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int node = curr[0], totalCost = curr[1], time = curr[2];

            if (node == n - 1) return totalCost;

            if (!graph.containsKey(node)) continue;

            for (int[] nei : graph.get(node)) {
                int next = nei[0], travel = nei[1];
                int newTime = time + travel;
                if (newTime <= maxTime && cost[next][newTime] > totalCost + passingFees[next]) {
                    cost[next][newTime] = totalCost + passingFees[next];
                    pq.offer(new int[]{next, cost[next][newTime], newTime});
                }
            }
        }
        return -1;
    }
}
