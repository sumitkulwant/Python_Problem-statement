n=int(input("Enter the rows:"))
c=ord("A")
for i in range(n):
    for j in range(i+1):
        print(chr(c),end="")
        c=c+1
    print()