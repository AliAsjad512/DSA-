class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0, time = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) q.offer(new int[]{r, c});
                if (grid[r][c] == 1) fresh++;
            }
        }

        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!q.isEmpty() && fresh > 0) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] curr = q.poll();
                for (int[] d : dirs) {
                    int nr = curr[0] + d[0], nc = curr[1] + d[1];
                    if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        q.offer(new int[]{nr, nc});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh == 0 ? time : -1;
    }
}
