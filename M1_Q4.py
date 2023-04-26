""" 4.write a program that reads n number and print the cube of N number from 1
input;
4

output:
1
8
27
64 """

N=int(input("Enter the value N:"))
for i in range(1,N+1):
    print("Square is ", i*i)
    print( "Cube of Numbers is ", i*i*i)
    print()

#Method2
cube=0
while cube<=N:
    print("Cube of Numbers is ", cube **3)
    cube+=1