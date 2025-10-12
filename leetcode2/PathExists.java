import java.util.*;

public class PathExists {
    static boolean dfs(int node, int dest, boolean[] visited, List<List<Integer>> adj) {
        if (node == dest) return true;
        visited[node] = true;

        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, dest, visited, adj)) return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] edges = {{0,1},{0,2},{3,4}};
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        boolean[] visited = new boolean[n];
        int src = 0, dest = 4;
        System.out.println("Path Exists: " + dfs(src, dest, visited, adj));
    }
}
