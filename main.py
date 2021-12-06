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