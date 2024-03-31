#creating a method to return fizz, buzz, or fizzbuzz
#returns fizz if number is divisable by 3
#returns buzz if number is divisable by 5
#returns fizzbuzz if number is divisable by 3 and 5
def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        print("FizzBuzz")
    elif input % 3 == 0:
        print('Fizz')
    elif input % 5 == 0:
        print('Buzz')
    else:
        print(input)

fizz_buzz(7)