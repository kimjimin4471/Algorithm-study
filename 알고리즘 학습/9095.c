#include<stdio.h>

int main() {
	int d[12];
	d[0] = 0;
	d[1] = 1;
	d[2] = 2;
	d[3] = 4;
	int n;
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		for (int j = 4; j <= n; j++) {
			d[j] = d[j - 1] + d[j - 2] + d[j - 3];
		}
		printf("%d\n", d[n]);
	}
}