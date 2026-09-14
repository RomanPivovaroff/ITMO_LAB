#include <cctype>
#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
  string word;
  string left;
  string right;
  unordered_map<string, long> context;
  stack<unordered_map<string, long>> history;
  unordered_map<string, long> context_edits;
  history.push({});
  while (cin >> word) {
    if (word == "{") {
      history.push({});
    } else if (word == "}") {
      context_edits = history.top();
      for (auto const& pair : context_edits) {
        context[pair.first] = pair.second;
      }
      history.pop();
    } else {
      size_t pos = word.find('=');
      left = word.substr(0, pos);
      right = word.substr(pos + 1);
      if (history.top().count(left) == 0) {
        history.top()[left] = context[left];
      }
      if (isdigit(right[0]) || right[0] == '-') {
        context[left] = stol(right);
      } else {
        cout << context[right] << endl;
        context[left] = context[right];
      }
    }
  }
  return 0;
}