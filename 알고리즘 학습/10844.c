#include<stdio.h>
#define MOD 1000000000;

int main() {
	int dp[101][10] = { 0, };
	for (int i = 1; i < 10; i++) {
		dp[1][i] = 1;
	}
	
	int n;
	scanf("%d", &n);
	
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			if (j == 0) {
				dp[i][j] = (dp[i - 1][j + 1]) % MOD;
			}
			else if (j == 9) {
				dp[i][j] = (dp[i - 1][j - 1]) % MOD;
			}
			else {
				dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD;
			}
		}
	}

	int cnt = 0;
	for (int i = 0; i < 10; i++) {
		cnt += dp[n][i] % MOD;
		cnt %= MOD;
	}
	printf("%d", cnt);
	return 0;
}