import java.util.*;

public class DetectCycle {
    static boolean dfs(int node, int parent, boolean[] visited, List<List<Integer>> adj) {
        visited[node] = true;
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, visited, adj)) return true;
            } else if (neighbor != parent) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        int n = 5;
        int[][] edges = {{0,1},{1,2},{2,3},{3,1}};
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        boolean[] visited = new boolean[n];
        boolean cycle = false;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && dfs(i, -1, visited, adj)) {
                cycle = true;
                break;
            }
        }

        System.out.println("Cycle Present: " + cycle);
    }
}
