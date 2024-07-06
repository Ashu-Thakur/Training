# different types of loops, nested loops, pass, continue, break in loops

#! If the current number is divisible by 2, skip the current iteration and move to the next number
for i in range(50):
    if i % 2 == 0 :
        continue
    print(i)

number = 0
while(number < 50):
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# !If the current number is greater than 50, stop the loop entirely (using break.
num = 1
while(True):
    if num > 50:
        break
    num += 1
    print(num)


# find the prime number till the given number
num = int(input("Enter the number :"))

for i in range(2, num):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end=" ")

# external factors

from datetime import datetime
now = datetime.now()
print("\n",now.hour,now.minute,now.second)
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")




