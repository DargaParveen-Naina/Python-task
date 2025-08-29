# Reverse a number and check palindrome

num1=int(input("Enter a number: "))
rev=0
temp=num1
while temp>0:
    digits=temp%10
    rev=rev*10+digits
    temp=temp//10
print(rev)
if num1==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

# print even digits

n=int(input("Enter a number: "))
while n>0:
    digit=n%10
    if digit%2==0:
        print(digit)
    n//=10

# print prime numbers in a given number

n=int(input("Enter a number: "))
while n>0:
    digit=n%10
    if digit in [2,3,5,7]:
        print(digit)
    n//=10

# Print perfect number

num=int(input("Enter a number: "))
sum_of_divisors=0
for i in range(1,num):
    if num%i==0:
        sum_of_divisors+=i
if sum_of_divisors==num:
    print("Perfect Numbers")
else:
    print("Not a perfect number")




