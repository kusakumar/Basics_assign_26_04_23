""" 10.Inverted right angled triangle

write a program that reads a number N and prints an inverted right angled triangle of N rows using start

input
5

output
* * * * *
* * * *
* * *
* *
*
"""
N=int(input("Enter the value M:"))
for i in range(N+1,0,-1):
    for j in range(0,i-1):
        print(" *",end=' ')
    print()

#Method2
print("\r")
for i in range(N+1,0,-1):
    for j in range(0,i-1):
        print("* " * i,end=" ")
        print()