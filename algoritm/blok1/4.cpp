#include <iostream>
#include <string>

using namespace std;

int main() {
  int a;
  int b;
  int c;
  int d;
  int k;
  cin >> a;
  cin >> b;
  cin >> c;
  cin >> d;
  cin >> k;
  for (int i = 0; i < k; i++) {
    a = min(d, max(0, a * b - c));
    if (a == 0) {
      break;
    }
    if (a == d) {
      break;
    }
    if (a == min(d, max(0, a * b - c))) {
      break;
    }
  }
  cout << a;
  return 0;
}