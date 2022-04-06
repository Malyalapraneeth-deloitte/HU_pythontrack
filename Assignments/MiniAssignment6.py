# generator code
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci_generator()
for i in fib:
    if i > 100:
        break
    else:
        print(i)



# decorator code
print('\n'"Decorator code")
def twice(function):
    def twiceExecution(number1,number2):
        function(number1,number2)
        function(number1,number2)
    return twiceExecution

@twice
def multiply(num1,num2):
    print(num1 * num2)
multiply(3,6)