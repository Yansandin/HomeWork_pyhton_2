print("Введите число s: ")
s= int(input())
print("Введите число p: ")
p=int(input())

for i in range(s):
    for j in range(p):
        if i+j==s and i*j==p:
            print(i,j)
            