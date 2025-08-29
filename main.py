## nested conditional statements
# activity 1
# fitness_response = input("Are you medically fit to take the exam (yes/no): ")
# if fitness_response == "yes":
#     print("You are allowed to take the exam")
# else:
#     attendance = int(input("Enter your attendance percentage: "))
#     if attendance >= 75:
#         print("You are allowed to take the exam")
#     else:
#         print("Sorry, you need at least 75% attendance to take the exam.")

# activity 2
# vehicle_type = input("Choose motorcycle or car: ")

# if vehicle_type == "motorcycle":

#     motorcycle_type = input("Choose sports, standard or cruiser: ")
#     if motorcycle_type == "sports":
#         print("You have chosen a sports motorcycle.")
#     elif motorcycle_type == "standard":
#         print("You have chosen a standard motorcycle.")
#     elif motorcycle_type == "cruiser":
#         print("You have chosen a cruiser motorcycle.")
#     else:
#         print("Invalid motorcycle type selected.")

# elif vehicle_type == "car":
#     car_type = input("Choose sedan, SUV or hatchback: ")
#     if car_type == "sedan":
#         print("You have chosen a sedan car.")
#     elif car_type == "SUV":
#         print("You have chosen an SUV car.")
#     elif car_type == "hatchback":
#         print("You have chosen a hatchback car.")
#     else:
#         print("Invalid car type selected.")
# else:
#     print("Invalid vehicle type selected.")

## loops
# for i in range(1, 10):
#     print(i)

# question - ask a natural number from the user and print the sum of the natural numbers till that number
# n = int(input("Enter a natural number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print("The sum of natural numbers till", n, "is:", sum)

# question - ask a natural number from the user and print all the natural numbers till 1 starting from the entered natural number
# n = int(input("Enter a natural number: "))
# for i in range(n, 0, -1):
#     print(i)

## while loop
# print from 1 to 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# infinite loop using while
# while True:
#     print("This is an infinite loop.")

# question - ask a number from the user and check for the number being an arstrong number or not. Print an appropriate message.
# examples of arstrong numbers are 0, 1, 153, 370, 371, 407
# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10
# if sum == num:
#     print(num, "is an Armstrong number.")
# else:
#     print(num, "is not an Armstrong number.")   

## nested loop
# num = 1
# for i in range(2, num):
#     if (num % i) == 0:
#         print("factor other than 1 and num itself is found")
#         break
# else: # else works only if the for loop is not terminated by a break statement
#     print("no factor other than 1 and num itself is found")

# question - take two natural numbers from the user and print all the prime numbers starting from the entered first number till the entered second number
# n1 = int(input("Enter the starting natural number: "))
# n2 = int(input("Enter the ending natural number: "))
# for num in range(n1, n2 + 1):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)

## pattern
# understanding how to print without going to the next line
print(1, end=" ")
print(2)
print(3)
print()
print(4)

# Floyd's triangle
rows = int(input("Enter the number of rows for Floyd's triangle: "))
f = 1
for r in range(1, rows + 1):
    for c in range(1, r + 1):
        print(f, end=" ")
        f = f + 1
    print()

## introduction to turtle
