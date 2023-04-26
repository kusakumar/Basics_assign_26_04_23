""" 7.write a program that reads two numbers M and N and prints the sum of N numbers from M

input
7
3

output:
25  """

M=int(input("Enter the value M:"))
N=int(input("Enter the value N:"))
Sum=0
for i in range(M,N+1):
    Sum+=i
print(Sum)