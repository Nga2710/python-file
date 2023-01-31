import os
def clrscr():
    os.system("clear")
    #os.system("clsr")
while True:
  try:
    x = int(input("x = "))
    break
  except ValueError:
    print("ValueError, try again!")
clrscr()
result = [str(int(x))]
while True:
  if x % 2 == 0:
    x = x / 2
  else:
    x = 3*x + 1
  if str(int(x)) in result:
    break
  else:
    result.append(str(int(x)))
print("\x20".join(result))