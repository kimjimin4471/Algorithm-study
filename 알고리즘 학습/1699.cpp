#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int n;
	int D[100001];
	cin >> n;
	D[0] = 0;
	D[1] = 1;
	D[2] = 2;
	for (int i = 3; i <= n; i++) {
		D[i] = i;
		for (int j = 1 ; j*j <= i; j++) {
			if (D[i] > D[i - j*j] + 1) {
				D[i] = D[i - j*j] + 1;
			}
		}
	}
	cout << D[n];
}