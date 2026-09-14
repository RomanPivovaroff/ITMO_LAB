#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N, K, temp, counter;
  cin >> N >> K;
  vector<int> sorted_list(N);
  for (int i = 0; i < N; i++) {
    cin >> sorted_list[i];
  }
  int min_dist = 0;
  int max_dist = sorted_list[N - 1] - sorted_list[0];
  int res = 0;
  while (min_dist <= max_dist) {
    int mid = (min_dist + max_dist) / 2;
    temp = sorted_list[0];
    counter = 1;
    for (int i = 1; i < N; i++) {
      if (sorted_list[i] - temp >= mid) {
        temp = sorted_list[i];
        if (++counter >= K) {
          break;
        }
      }
    }
    if (counter >= K) {
      res = mid;
      min_dist = mid + 1;
    } else {
      max_dist = mid - 1;
    }
  }
  cout << res;
  return 0;
}