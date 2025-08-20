#Armstrong numbers range from 100 to 2000

m=int(input("Enter a number: "))
n=int(input("Enter a number: "))
for num in range(m,n+1):
    order=len(str(num))
    sum_of_powers=sum(int(digit)**order for digit in str(num))
    if num==sum_of_powers:
        print(num,end=" ")
        
#153
#370
#371
#407
#1634

#Prime Numbers range from 100 to 2000

m=int(input("Enter m: "))
n=int(input("Enter n: "))
for num in range(m,n+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
        else:
            print(num,end=" ")