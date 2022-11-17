x = int(input("Enter 1 number: "))
y = int(input("Enter 2 number: "))

if x>y:
    lower = y
else:
    lower = x

for i in range(1,lower+1):
    if((x%i == 0) and y%i == 0):
        hcf = i

print(i)