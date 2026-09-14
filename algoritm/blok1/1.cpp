#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;
  int num;
  int pastnum = 0;
  int povt_num_counter = 1;
  int start = 0;
  int max_start = 0;
  int max_end = 0;
  cin >> t;
  for (int i = 0; i < t; i++) {
    cin >> num;
    if (num == pastnum) {
      povt_num_counter += 1;
      if (povt_num_counter == 3) {
        if (max_end - max_start < i - start - 1) {
          max_start = start;
          max_end = i - 1;
        }
        start = i - 1;
        povt_num_counter = 2;
      }
    } else {
      povt_num_counter = 1;
    }
    if (i == t - 1) {
      if (max_end - max_start < i - start) {
        max_start = start;
        max_end = i;
      }
    }
    pastnum = num;
  }
  cout << max_start + 1 << " " << max_end + 1;
  return 0;
}