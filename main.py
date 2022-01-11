from modules import calcMod
from modules import modTemp



currentver = 0.01
print("cvx:", currentver)
print("________________")
loadmodule = input("Load Module? [y/n]")
if loadmodule == "y":
  print("Module?:")
  moduleask = input("")
elif loadmodule == "n":
  print("no modules loading")
else:
  print("Unexpected error has occured")
if moduleask == "ihCalc":
  print("modules.calcMod(load)")
elif moduleask == "modTemp":
  print("This is the template module")
else:
  print("an error has occured")
