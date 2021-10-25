#include<iostream>
using namespace std;

int main() {
	int arr[1001];
	int D[1001];
	int n, tmp;
	int max = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	D[0] = arr[0];

	for (int i = 1; i < n; i++) {
		D[i] = arr[i];
		for (int j = i - 1; j >= 0; j--) {
			if (arr[i] > arr[j]) {
				if (D[i] < D[j] + arr[i]) {
					D[i] = D[j] + arr[i];
				}
			}
		}
	}
	max = D[0];
	for (int i = 1; i < n; i++) {
		if (max < D[i]) {
			max = D[i];
		}
	}

	cout << max;
}