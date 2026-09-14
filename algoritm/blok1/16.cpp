#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int N;
  cin >> N;

  vector<pair<int, pair<int, int>>> edges;
  vector<vector<int>> matrix(N, vector<int>(N));
  for (int i = 0; i < N; i++)
    for (int j = 0; j < N; j++)
      cin >> matrix[i][j];

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i < j) {
        pair<int, int> vertices = {i, j};
        edges.push_back({min(matrix[i][j], matrix[j][i]), vertices}); // изменено
      }
    }
  }
  sort(edges.begin(), edges.end());
  vector<int> parent(N);
  for (int i = 0; i < N; i++)
    parent[i] = i;
  int components = N;
  int answer = 0;
  for (auto e : edges) {
    int w = e.first;
    int u = e.second.first;
    int v = e.second.second;
    int pu = u;
    int pv = v;
    while (parent[pu] != pu)
      pu = parent[pu];
    while (parent[pv] != pv)
      pv = parent[pv];
    if (pu != pv) {
      parent[pv] = pu;
      components--;
      answer = w;
      if (components == 1)
        break;
    }
  }
  cout << answer;
  return 0;
}