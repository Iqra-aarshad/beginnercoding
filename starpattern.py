# Half Pyramid
num = int(input("enter a number:"))
i = 1
while i <= num:
    print(i*"*")
    i = i + 1

# Inverted Half Pyramid
num = int(input("enter a number:"))
i = 1
j = num
while i <= num:
    print(j* "*"+" "*i)
    i +=1
    j -=1

# Full pyramid
num = int(input("enter a number:"))

for i in range(num):
    print(" " * (num-i-1) + "*"*(2*i+1))

# Hour glass pattern
num = int(input("enter the number of rows:"))
for i in range(num):
    print(" " * i + "* " * (num-i))
for i in range(num-2,-1,-1):
    print(" " * i + "* " * (num-i))

# Square pattern
num = int(input("enter the number of rows:"))
for i in range(num):
    for j in range(num):
        print("* ",end="")
    print()

# Diamond pattern
num = int(input("enter the number of rows:"))
for i in range(num):
    print(" " * (num-i-1) + "* " * (i+1))
for i in range(num-2,-1,-1):
    print(" " * (num-i-1) + "* " * (i+1)) 


