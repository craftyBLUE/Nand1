memoryIOReservedBits = 256

memoryIO = { #position in memory
    "output": 16, # byte
    "outputWrite": 3, #bit
    "input": 24, #byte
    "inputRead": 4 #bit
}

def stringToBinary(tempStr): #returns string of 0s and 1s of ascii text
    return ''.join(format(ord(char), '08b') for char in tempStr)

#reserve [1] as helper variable
def setReg(x):
    if x:
        return "1 0 1 1"
    else:
        return "1 0 1 1 0"

def copy(a):
    return f"{setReg(1)} {a} 0 {a} 0"

def paste(a): #write and keep, "a" is just write
    return f"{a} {copy(a)}"

def nand(out, a, b):
  return f"{copy(a)} {out} {copy(b)} {out} {out}"

def inputRead():
  return f"{setReg(1)} {memoryIO['inputRead']}"

def outputWrite():
  return f"{setReg(1)} {memoryIO['outputWrite']}"

def halt():
  return f"{setReg(1)} 2"

def prints(s): #print string
  outString = ""
  s = stringToBinary(s)

  for i in range(len(s) // 8):
      for j in range(8):
          ij = i * 8 + j
          if s[ij]=="1":
              outString += f"{setReg(1)} {j + memoryIO['output']} "
          else:
              outString += f"{setReg(0)} {j + memoryIO['output']} "
      outString += f"{setReg(1)} {memoryIO['outputWrite']}\n"

  return outString

if __name__ == "__main__":
  print(prints(input()))
  print(halt())
