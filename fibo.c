#include <stdio.h>

int memo[100];

int memoFibo(int n) {
	if (n <= 1) {
		return n;
	}
	else {
		if (memo[n] > 0) {
			return memo[n];
		}
		memo[n] = fibo(n - 1) + fibo(n - 2);
		return memo[n];
	}
}


int fibo(int n) {
	if (n <= 1) {
		return n;
	}
	else {
		return fibo(n - 1) + fibo(n - 2);
	}
}

int main() {
	
	printf("%d", memoFibo(38));

	return 0;
}