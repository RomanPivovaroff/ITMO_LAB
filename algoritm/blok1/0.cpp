#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;
  string word;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> word;
    if (word.size() % 2 == 0) {
      size_t half = word.size() / 2;
      if (word.substr(0, half) == word.substr(half)) {
        cout << "YES" << endl;
      } else {
        cout << "NO" << endl;
      }

    } else {
      cout << "NO" << endl;
    }
  }
  return 0;
}