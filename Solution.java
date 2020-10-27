import java.util.Arrays;
public class Solution {
    static int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        if (m == 0 | n == 0) {
            return 0;
        }
        if (obstacleGrid[0][0] == 1) {
            return 0;
        }

        int[][] map = new int[m][n];
        map[0][0] = 1;
        for (int i = 0; i < m; i++) {
            if (obstacleGrid[i][0] == 1) {
                map[i][0] = 0;
            } else {
                map[i][0] = 1;
            }
        }
        for (int j = 0; j < n; j++) {
            if (obstacleGrid[0][j] == 1) {
                map[0][j] = 0;
            } else {
                map[0][j] = 1;
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                map[i][j] = obstacleGrid[i][j] == 1 ? 0 : map[i - 1][j] + map[i][j - 1];
            }
        }
        System.out.println(Arrays.deepToString(map));
        System.out.println(Arrays.deepToString(obstacleGrid));
        return map[m - 1][n - 1];
    }

    public static void main(String[] args) {
        int[][] data = { { 0, 0, 0 }, { 0, 1, 0 }, { 0, 0, 0 } };
        uniquePathsWithObstacles(data);
    }
}

