#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

char memory[1 << 29]; // 2^32 bits
bool get(int pos) {
  return memory[pos / 8] & (1 << (7 - pos % 8));
}
void set(int pos, bool value) {
  memory[pos / 8] = memory[pos / 8] & ~(1 << (7 - pos % 8)) | ((int)value << (7 - pos % 8));
}

bool nand(bool x, bool y) {
  return not (x and y);
}

int a, b;

vector<int> commands = {};
int ci = 0;

/* MemoryIO map
0 -> register
1 -> helper register
2 -> signal halt
3 -> signal outputWrite
4 -> signal inputRead
5..15 -> reserved
16..23 -> output char
24..32 -> input char
*/
void memoryIO() {
  if (get(3)) { // outputWrite (bit)
    if (memory[2]) { // null edge case
      printf("%c", memory[2]); // bits [16, 23]
    }
    set(3, 0);
  }
  if (get(4)) { // inputRead (bit)
    char tempChar;
    scanf("%c", &tempChar); // bits [24, 31]
    memory[3] = tempChar;
    set(4, 0);
  }
  return;
}

int main(int argc, char* argv[]) {
  if (argc < 2) {
    printf("No source code specified!\n");
    return -1;
  }
  
  ifstream sourceCode(argv[1]);
  while (sourceCode >> a) {
    commands.push_back(a);
  }
  sourceCode.close();
  
  while (not get(2)) { //halt when value at position 2 is = 1
    a = commands[ci];
    b = nand(get(0), get(a));
    set(a, get(0));
    set(0, b);
    
    memoryIO();
    
    ci++;
    ci %= commands.size();
  }
  return 0;
}
