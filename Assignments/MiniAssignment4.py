# Solving Quadration equation using Lambda function

val = lambda x, a, b, c: (a * (x * x)) + (b * x) + c
print("solution for equation ( (a * (x * x)) + (b * x) + c ) using lambda function is ")
print(val(1, 2, 3, 4))
print()


# Occurance of characters in list using count() Lambda and map()

list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
result = map(lambda x: [x.count("A"), x.count('a')], list1)
print("occurrence of characters of A and a are ")
print(list(result))


