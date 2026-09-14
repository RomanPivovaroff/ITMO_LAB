#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N, temp, pos;
  int res = 0;
  cin >> N;
  vector<int> graph(N);
  vector<int> visited(N, 0);
  for (int i = 0; i < N; i++) {
    cin >> temp;
    graph[i] = temp - 1;
  }
  for (int i = 0; i < N; i++) {
    if (visited[i] != 0) {
      vector<int> path;
      pos = i;
      while (visited[pos] == 0) {
          visited[pos] = 1;
          path.push_back(pos);
          pos = graph[pos];
      }
      if (visited[pos] == 1) res++;
      for (int v : path) visited[v] = 2;
      visited[pos] = 2;
    }
  }
  cout << res;
  return 0;
}