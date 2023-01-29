import os
def clrscr():
    os.system("clear")
    #os.system("clsr")
while True:
  try:
    x = int(input("x = "))
    if x > 0:
      break
  except ValueError:
    print("ValueError, try again!")
clrscr()
result = []
while x != 1:
  result.append(str(int(x)))
  if x % 2 == 0:
    x = x / 2
  else:
    x = 3*x + 1
print("\x20".join(result))