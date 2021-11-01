#include<iostream>
using namespace std;

int MAX(int a, int b) {
	if (a > b) return a;
	return b;
}

int main() {
	int D[301];
	int n, arr[301];
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	D[1] = arr[1];
	D[2] = arr[1] + arr[2];
	D[3] = MAX(arr[1] + arr[3], arr[2] + arr[3]);

	for (int i = 4; i <= n; i++) {
		D[i] = MAX(D[i - 2] + arr[i], D[i - 3] + arr[i - 1] + arr[i]);
	}

	cout << D[n];
}