# Input
> A

A is a nonnegative integer in base 10, it represents a location in memory.  
The result from the binary operation `[0] NAND a` is stored at location `0`. The **old value** from location 0 is moved to position A. 
`a` here is the value at position `A`; `[0]` is value at position `0`  
Input is repeated until the program halts. (A1 A2 A3 A4 A5 A6 ...)  
4294967296 (=2^32) bits of memory are available.  
Memory does not guarantee any initial state.  
Setting value 1 to location `2` in memory halts the program and also dumps the memory to stdout.  

See also  
[craftyBLUE/Nand32](https://github.com/craftyBLUE/Nand32)  
[craftyBLUE/Nand2](https://github.com/craftyBLUE/Nand2)