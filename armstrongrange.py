m=int(input("Enter a number: "))
n=int(input("Enter a number: "))
for num in range(m,n+1):
    order=len(str(num))
    sum_of_powers=sum(int(digit)**order for digit in str(num))
    if num==sum_of_powers:
        print(num,end=" ")