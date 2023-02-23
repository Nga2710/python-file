a = float(input("Nhập cạnh a:"))
b = float(input("Nhập cạnh b:"))
c = float(input("Nhập cạnh c:"))
if a > 0 and b > 0 and c > 0 and a+b>c and a+c>b and b+c>a:
    p = (a+b+c)/2
    print("Chu vi tam giác:",p*2,"; Diện tích tam giác:", (p*(p-a)*(p-b)*(p-c))**0.5)
else:
    print("Không phải là ba cạnh của một tam giác")
