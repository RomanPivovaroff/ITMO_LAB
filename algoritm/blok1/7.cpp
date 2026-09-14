#include <algorithm>
#include <cctype>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main() {
  string word;
  int tmp_weight;
  cin >> word;
  vector<pair<int, char>> letter_weights;
  map<char, int> frequency_table;
  string right = "";
  string left = "";
  string middle = "";
  for (int i = 0; i < 26; i++) {
    cin >> tmp_weight;
    letter_weights.push_back({tmp_weight, ('a' + i)});
  }
  sort(letter_weights.rbegin(), letter_weights.rend());
  for (size_t i = 0; i < word.size(); i++) {
    frequency_table[word[i]]++;
  }
  for (auto it = letter_weights.begin(); it != letter_weights.end(); it++) {
    if (frequency_table.count(it->second)) {
      if (frequency_table[it->second] >= 2) {
        frequency_table[it->second] -= 2;
        right = it->second + right;
        left = left + it->second;
        if (frequency_table[it->second] > 0) {
          middle += string(frequency_table[it->second], it->second);
        }
      } else {
        middle += it->second;
      }
    }
  }
  cout << left << middle << right;
  return 0;
}