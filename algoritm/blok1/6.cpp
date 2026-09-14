#include <cctype>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string word;
  cin >> word;
  vector<string> results = {word};
  while (cin >> word) {
    bool flag = true;
    for (size_t i = 0; i < results.size(); i++) {
      if (results[i] + word < word + results[i]) {
        results.insert(results.begin() + i, word);
        flag = false;
        break;
      };
    };
    if (flag) {
      results.push_back(word);
    }
  };
  for (size_t i = 0; i < results.size(); i++) {
    cout << results[i];
  }
  return 0;
}