a = float(input("Nhập hệ số a:"))
while a == 0:
  print("Hệ số a phải khác 0, nhập lại!")
  a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))
delta = b**2-4*a*c
if delta == 0:
  print("Phương trình có nghiệm kép x = " + str(-b/(2*a)))
if delta < 0:
  print("Phương trình vô nghiệm")
if delta > 0:
  print("Phương trình có hai nghiệm phân biệt: x1 = ", (-b-delta**0.5)/(2*a), ";x2 = ", (-b+delta**0.5)/(2*a))
