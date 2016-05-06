#problema 30
#b<=1
#print(a)
a = int(input("a: "))
b = int(input("b: "))
while a <= 0 or b <= 0:
    a = int(input("a= "))
    b = int(input("b= "))

while b >= 1:
    c = a % b
    a = b
    b = c
print(a)    