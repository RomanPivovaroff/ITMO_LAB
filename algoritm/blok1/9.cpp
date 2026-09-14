#include <deque>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
  int N, P, temp, maxInd;
  size_t K;
  int counter = 0;
  cin >> N >> K >> P;
  vector<deque<int>> cars(N);
  unordered_set<int> floor;
  vector<int> commands(P);
  for (int i = 0; i < P; i++) {
    cin >> temp;
    cars[temp].push_back(i);
    commands[i] = temp;
  }
  for (int i = 0; i < P; i++) {
    if (floor.find(commands[i]) == floor.end()) {
      if (floor.size() == K) {
        maxInd = *floor.begin();
        for (int car : floor) {
          if (cars[car].empty()) {
            maxInd = car;
            break;
          } else {
            if (cars[car].front() > cars[maxInd].front()) {
              maxInd = car;
            }
          }
        }
        floor.erase(maxInd);
      }
      floor.insert(commands[i]);
      counter++;
    }
    cars[commands[i]].pop_front();
  }
  cout << counter;
  return 0;
}