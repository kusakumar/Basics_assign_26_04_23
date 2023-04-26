""" 4.square 
write a program that reads a number M and prints a square of M and M column using stars

sample input
4 

output 
* * * *
* * * *
* * * * """
M=int(input("Enter the value M:"))
for i in range(1,M+1):
    print(" *"*M)