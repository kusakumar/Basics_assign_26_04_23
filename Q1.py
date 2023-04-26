"""1. write a program that reads a number N and prints 10 numbers after N 
sample input
5
output:
5
6
7
8
9
10 .... upto numbers  """
N=int(input("Enter N value: "))
for i in range(1,11):
    print(N-1+i)