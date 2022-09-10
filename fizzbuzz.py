# My coder friends challenged me to write a fizz buzz program.
# Fizz Buzz Challenge: Write a program that prints 1 to 100, but for:
# Multiples of 3, print "Fizz"
# Multiples of 5, print "Buzz"
# Multiples of both 3 and 5, print "FizzBuzz"

# My solution:
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        i += 1
    elif i % 3 == 0:
        print('Fizz')
        i += 1
    elif i % 5 == 0:
        print('Buzz')
        i += 1
    else:
        print(i)
        i += 1

# Here is a more efficient answer:
for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)
