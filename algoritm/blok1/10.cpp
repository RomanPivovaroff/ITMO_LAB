#include <cctype>
#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {
  int N, ind;
  char comm;
  cin >> N;
  deque<int> start;
  deque<int> end;
  for (int i = 0; i < N; i++) {
    cin >> comm;
    if (comm == '+') {
      cin >> ind;
      end.push_back(ind);
    }
    else if (comm == '*') {
      cin >> ind;
      start.push_back(ind);
    }
    else {
      cout << start.front() << endl;
      start.pop_front();
    }
    if (start.size() > 1 +  end.size()) {
      end.push_front(start.back());
      start.pop_back();
    }
    else if (start.size() < end.size()) {
      start.push_back(end.front());
      end.pop_front();
    }
  }
  return 0;
}