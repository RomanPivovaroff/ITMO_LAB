#include <algorithm>
#include <cctype>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main() {
  int N, K;
  int res = 0;
  cin >> N >> K;
  vector<int> prices(N);
  for (int i = 0; i < N; i++) {
    cin >> prices[i];
  }
  sort(prices.rbegin(), prices.rend());
  for (int i = 0; i < N; i++) {
    if ((i + 1) % K != 0) {
      res += prices[i];
    }
  }
  cout << res;
  return 0;
}