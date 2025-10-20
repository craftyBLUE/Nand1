#include <iostream>
using namespace std;

char memory[1 << 29]; // 2^32 bits
bool get(int pos) {
  return memory[pos / 8] & (1 << (pos % 8));
}
void set(int pos, bool value) {
  memory[pos / 8] = memory[pos / 8] & ~(1 << (pos % 8)) | ((int)value << (pos % 8));
}

bool nand(bool x, bool y) {
  return not (x and y);
}

int a, b;

int main() {
  while (not get(2)) { //halt when value at position 2 is = 1
    cin >> a;
    b = nand(get(0), get(a));
    set(a, get(0));
    set(0, b);
  }
  for (int i = 1; i < (1 << 29); i++) {
    if (memory[i]) {
      printf("%c", memory[i]);
    }
  }
  printf("\n");
  return 0;
}
