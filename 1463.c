#include<stdio.h>

int d[1000001];

int main() {
	d[0] = 0;
	d[1] = 0;
	int min;
	int n;
	scanf("%d", &n);
	for (int i = 2; i <= n; i++) {
		min = d[i - 1];
		if (i % 2 == 0 & min > d[i / 2]) {
			min = d[i / 2];
		}
		if (i % 3 == 0 & min > d[i / 3]) {
			min = d[i / 3];
		}
		d[i] = min + 1;
	}
	printf("%d", d[n]);
}