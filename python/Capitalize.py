s = input("Enter the string : ")

a = s.split(" ")
b = []

for i in a:
    b.append(i.capitalize())

c = " ".join(b)

print(c)