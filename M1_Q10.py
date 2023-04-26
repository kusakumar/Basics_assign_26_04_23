"""  10. given a number n,write a program that reads n numbers as input and prints the product of the given n numbers.

input:
	n=3
	2
	3
	7
output:
 	2*3*7=42 """
N=int(input("Enter the value N:"))
prod=1
for i in range(1,N+1):
    nums =int(input("enter elt: "))
    prod*=nums
    print()
print(prod)
