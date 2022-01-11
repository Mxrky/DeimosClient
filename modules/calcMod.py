modName = "basicCalc"

def BASICtabinput():
  inp1 = input("int1")
  inp2 = input("int2")
  operation = input("+, -, x, /")
  if operation == "+":
    print(inp1 + inp2)
  elif operation == "-":
    print(inp1 - inp2)