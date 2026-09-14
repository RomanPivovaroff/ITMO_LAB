#include <deque>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
  int N, P, temp, K;
  int counter = 0;
  cin >> N >> K >> P;

  vector<deque<int>> cars(N);
  vector<bool> onFloor(N, false);
  priority_queue<pair<int, int>> pq;
  vector<int> nextIdx(N, 1e9);
  int car_on_floor = 0;
  vector<int> commands(P);

  for (int i = 0; i < P; i++) {
    cin >> temp;
    temp--;
    cars[temp].push_back(i);
    commands[i] = temp;
  }

  for (int i = 0; i < P; i++) {
    int car = commands[i];
    cars[car].pop_front();

    if (!onFloor[car]) {
      counter++;
      if (car_on_floor == K) {
        while (!pq.empty()) {
          auto [future, c] = pq.top();
          if (onFloor[c] && nextIdx[c] == future)
            break;
          pq.pop();
        }
        auto [future, victim] = pq.top();
        pq.pop();
        onFloor[victim] = false;
        car_on_floor--;
      }
      int next = cars[car].empty() ? 1e9 : cars[car].front();
      onFloor[car] = true;
      nextIdx[car] = next;
      pq.push({next, car});
      car_on_floor++;
    } else {
    int next = cars[car].empty() ? 1e9 : cars[car].front();
    nextIdx[car] = next;
    pq.push({next, car});
    }
  }

  cout << counter;
  return 0;
}