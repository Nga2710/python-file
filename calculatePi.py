n = 3
p = 1
i = 0
def cal(n):
  return 2/(-n*(n+2))
while True:
  for k in range(0, 39997, 4):
    p = p+cal(n+k)
  n += 40000
  i += 1
  if i % 100 == 0:
    print(str(i) + " | " + str(p*4))