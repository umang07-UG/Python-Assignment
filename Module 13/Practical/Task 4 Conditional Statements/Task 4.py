# 5)  Practical Example 5: Write a Python program to find greater and less than a number using if_else

first_number = int(input("Enter First Number : "))
second_number = int(input("Enter Second Number : "))

if first_number<second_number:
    print(second_number,"Is Greater")
else:
    print(first_number,"Is Grater")


# 6)  Practical Example 6: Write a Python program to check if a number is prime using if_else.


n=int(input("Enter Number : "))
prime=0
for i in range(1,n+1):
    if n%i==0:
        prime=prime+1
if (prime==2):
    print(n," is Prime number")
else:
    print(n,"Is not prime Number")


#  7)  Write a Python program to calculate grades based on percentage using if-else ladder.


 percentage = float(input("Enter your percentage: "))

 if percentage >= 90:
     print("Grade: A+")
 elif percentage >= 80:
     print("Grade: A")
 elif percentage >= 70:
     print("Grade: B")
 elif percentage >= 60:
     print("Grade: C")
 elif percentage >= 50:
     print("Grade: D")
 else:
     print("Grade: F (Fail)")


# 8)  Practical Example 8: Write a Python program to check if a person is eligible to donate blood using nested if


age=int(input("Enter Your Age "))

if age>=70:
    print("You are old, you cannot donate blood.")

elif age>=18:
    print("You Are Eligible To Donate Blood")
else:
    print("You are not eligible to donate blood because you are under 18")