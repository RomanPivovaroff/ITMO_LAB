#include <cctype>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int main() {
  string word;
  char letter;
  char nowletter;
  stack<size_t> traps;
  int animal_counter = 1;
  cin >> word;
  vector<size_t> animal_nums(word.size());
  vector<int> results(word.size(), 0);
  for (size_t i = 0; i < word.size(); i++) {
    letter = word[i];
    if (letter >= 'A' && letter <= 'Z') {
      nowletter = tolower(letter);
    } else {
      animal_nums[i] = animal_counter++;
      nowletter = toupper(letter);
    }
    if (!traps.empty()) {
      if (word[traps.top()] == nowletter) {
        results[isupper(letter) ? i : traps.top()] =
            islower(letter) ? animal_nums[i] : animal_nums[traps.top()];
        traps.pop();
      } else {
        traps.push(i);
      }
    } else {
      traps.push(i);
    }
  }
  if (traps.empty()) {
    cout << "Possible" << endl;
    for (size_t i = 0; i < word.size(); i++) {
      if (isupper(word[i])) {
        cout << results[i] << " ";
      }
    }
  } else {
    cout << "Impossible";
  }
  return 0;
}