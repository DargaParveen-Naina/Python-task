n=int(input("Enter a number:"))
power=len(str(n))
sum_of_digits=0
for digits in str(n):
    sum_of_digits+=int(digits)**power
if n==sum_of_digits:
    print(n,"is a Armstrong Number")
else:
    print(n,"is not a Armstrong Number")
