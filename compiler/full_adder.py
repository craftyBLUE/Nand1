from nand1_text_universal import *

def fullAdder(
    a,
    b,
    carryIn,
    carryOut,
    out,
    helperStart = memoryIOReservedBits
  ):
  #reserve 6 helper variables
  helperD = helperStart + 0
  helperE = helperStart + 1
  helperF = helperStart + 2
  helperG = helperStart + 3
  helperH = helperStart + 4
  helperI = helperStart + 5
  outString = ""
  
  outString += f"{copy(a)}\n"
  outString += f"{helperD}\n"
  outString += f"{copy(b)}\n"
  outString += f"{helperE}\n"
  outString += f"{copy(carryIn)}\n"
  outString += f"{helperF}\n"
  outString += f"{nand(helperG, helperD, helperE)}\n"
  outString += f"{nand(helperH, helperD, helperG)}\n"
  outString += f"{nand(helperI, helperG, helperE)}\n"
  outString += f"{nand(helperD, helperH, helperI)}\n"
  outString += f"{nand(helperE, helperD, helperF)}\n"
  outString += f"{nand(helperH, helperD, helperE)}\n"
  outString += f"{nand(helperI, helperE, helperF)}\n"
  outString += f"{nand(carryOut, helperE, helperG)}\n"
  outString += f"{nand(out, helperH, helperI)}\n"
  
  return outString

def main():
  print(inputRead(), copy(memoryIO["input"] + 7), 1001) # a
  print(inputRead(), copy(memoryIO["input"] + 7), 1002) # b
  print(inputRead(), copy(memoryIO["input"] + 7), 1003) # carryIn

  print(fullAdder(
    1001, # a
    1002, # b
    1003, # carryIn
    1004, # carryOut
    1005  # out
  ))

  #prepare for copy
  print(setReg(1), memoryIO["output"] + 2)
  print(setReg(1), memoryIO["output"] + 3)

  print(copy(1004), memoryIO["output"] + 6) # carryOut
  print(copy(1005), memoryIO["output"] + 7) # out
  print(outputWrite())

  print(halt())

if __name__ == "__main__":
  main()
