import java.util.*;

public class ConnectedComponents {
    static void dfs(int node, boolean[] visited, List<List<Integer>> adj) {
        visited[node] = true;
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) dfs(neighbor, visited, adj);
        }
    }

    public static void main(String[] args) {
        int n = 6;
        int[][] edges = {{0,1},{2,3},{3,4}};
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());

        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        boolean[] visited = new boolean[n];
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, visited, adj);
                count++;
            }
        }

        System.out.println("Connected Components: " + count);
    }
}
