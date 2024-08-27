# 1. Write a program to display the multiplication table for a number 
#number is taken as input
#use while loop
num = int(input("Enter the number"))
i = 1
while i<=10:
    print(num, "X", i, "=", num*i)
    i = i+1
print("End of multiplication table")

# 2. Write a python to reverse a number using while loop
n = int(input("num="))
reverse = 0
while n !=0:
    rem = n%10
    reverse=reverse*10+rem
    n = n//10
print(reverse)

# 3. Write a program to convert a decimal number to binary
a = int(input("enter num:"))
result = ""
while a!=0:
    l = a%2
    a = a//2
    r = a
    result = str(l) + result
print(result)

# 4. Write a program to find the sum of n numbers using a while loop
num = int(input("enter number"))
sum = 0
while num !=0:
     sum = sum + num
     num -= 1
print(sum) 

#4. Method 2
#num = int(input("Number:"))
#sum = 0
#while :
#     sum



#5. wap to to display sum of odd and even separately that falls between a range of 2 intgers
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
e = 0
o = 0
while num1 <= num2:
     if num1%2 == 0:
        e = e + num1
        num1 = num1 + 1
     else:
          o = o + num1
          num1 = num1 + 1   
print("sum of even numbers is", e)
print("Sum of odd numbers is", o)

#6. wap to display all the prime numbers in the rangle 100 to 200 using for loop
for n in range (100,201):
    for y in range(2,n):
        if n%y ==0:
            break
        else:
            print(n)
            break


