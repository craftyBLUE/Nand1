# Input
> A

A is a nonnegative integer in base 10, it represents a location in memory.  
The result from the binary operation `[0] NAND a` is stored at location `0`. The **old value** from location 0 is moved to position A. 
`a` here is the value at position `A`; `[0]` is value at position `0`    
4294967296 (=2^32) bits of memory are available.  
Memory does not guarantee any initial state.  
When the end of the source file is reached it repeats the commands from the start but keeping the current memory state.

# Memory I/O
## Halt
Setting value 1 to location `2` in memory halts and exits the program.

## Output
Setting value 1 to location `3` in memory prints to the screen the ascii character located between and including location `16` and `23`. 

## Input
Setting value 1 to location `4` in memory inputs an ascii character from the keyboard and puts its binary values between and including positions `24` and `31` in memory.  

# Running code
Put your Nand1 code in a file with a `.nand1` extension and run it like so:  
> nand1.exe hello_world.nand1  

> ./nand1 hello_world.nand1  

See also  
[craftyBLUE/Nand32](https://github.com/craftyBLUE/Nand32)  

[craftyBLUE/Nand2](https://github.com/craftyBLUE/Nand2)
