import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] orders = new int[N][2]; // {거리, 예민도}

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            orders[i][0] = Integer.parseInt(st.nextToken());
            orders[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(orders, (a, b) -> {
            long x = (2 * a[0] + 1) * b[1];
            long y = (2 * b[0] + 1) * a[1];

            return Long.compare(x, y);
        });

        long totalTime = 0;
        long sum = 0;

        for (int i = 0; i < N; i++) {
            totalTime += orders[i][0];
            sum += (long)orders[i][1] * (totalTime + i);
            totalTime += orders[i][0];
        }

        System.out.println(sum);
    }
}
