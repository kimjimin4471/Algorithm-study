#include<stdio.h>

int arr[1001] = { 0, };
int dp[1001] = { 0, };

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}
	dp[0] = 0;
	dp[1] = arr[1];
	for (int i = 2; i <= n; i++) {
		dp[i] = arr[i];
		for (int j = 1; j < i; j++) {
			if (dp[i - j] + arr[j] >= dp[i]) {
				dp[i] = dp[i - j] + arr[j];
			}
		}
	}
	printf("%d", dp[n]);
	return 0;
}