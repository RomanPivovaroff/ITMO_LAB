#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N, K, temp;
  deque<int> mins;
  cin >> N >> K;
  vector<int> din_arr(N);
  for (int i = 0; i < N; i++) {
    cin >> temp;
    din_arr[i] = temp;

    if (!mins.empty() && mins.front() <= i - K) {
      mins.pop_front();
    }
    while (!mins.empty() && din_arr[mins.back()] >= temp) {
      mins.pop_back();
    }
    mins.push_back(i);
    if (i >= K - 1) {
      cout << din_arr[mins.front()] << ' ';
    }
  }
  return 0;
}