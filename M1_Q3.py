""" 3.Average of the N number

Input:
4
out:
2.5 """
N = int(input("Enter the value N:"))
sum=0
for i in range(0, N + 1):
    sum += i
Avg = sum / N
print(Avg)
