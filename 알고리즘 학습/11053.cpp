#include<iostream>
using namespace std;

int main() {
	int arr[1001];
	int D[1001] = { 1, };
	int n;
	int max = 0;
	cin >> n;
	D[0] = 1;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 1; i < n; i++) {
		D[i] = 1;
		for (int j = i - 1; j >= 0; j--) {
			if (arr[i] > arr[j]) {
				if (D[i] < D[j] + 1) {
					D[i] = D[j] + 1;
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