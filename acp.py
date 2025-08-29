## nested conditional statements
# question - design a voter eligibility checking system. First the system should ask the person whether he is the country's citizen or not. If not then print like "You need to be a Indian citizen to vote". If yes, then ask for age. If the age is more than or equal to 18, tell the person that he is allowed to vote. If the user is less than 18, then print the appropriate message.
# is_citizen = input("Are you an Indian citizen? (yes/no): ")

# if is_citizen.lower() == "yes":
#     age = int(input("Please enter your age: "))
#     if age >= 18:
#         print("You are allowed to vote.")
#     else:
#         print("You need to be at least 18 years old to vote.")
# else:
#     print("You need to be an Indian citizen to vote.")

## loops
# question - take two natural numbers from the user and print all the even numbers starting from the entered first number till the entered second number
# start = int(input("Enter the starting natural number: "))
# end = int(input("Enter the ending natural number: "))
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(i)

## while loop
# question - take a natural number from the user and print the number of digits the number is having. use while loop
# num = int(input("Enter a natural number: "))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print("The number of digits is:", count)

## nested loop
# question - continue to ask a number from user until the user enters a number that is a prime number
# while True:
#     num = int(input("Enter a natural number: "))
#     for i in range(2, int(num**0.5) + 1):
#         if (num % i) == 0:
#             print(num, "is not a prime number. Please try again.")
#             break
#     else:
#         print(num, "is a prime number.")
#         break

## pattern
# question - print mirrored right angled triangle of stars
rows = int(input("Enter the number of rows for mirrored right angled triangle: "))
for r in range(1, rows + 1):
    print(" " * (rows - r), end="")
    print("*" * r)

## introduction to turtle