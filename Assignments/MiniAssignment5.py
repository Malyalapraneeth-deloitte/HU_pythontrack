#multiplication of the list
from functools import reduce
def multiplication(a,b):
    return a*b
lst = [1,2,3,4,5,6,7,8,9]
result = reduce(multiplication, lst)
print("result is : ", result,"\n")

# creating key value pairs using zip and dictionary functions
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
Dictionary = dict(zip(lst1, lst2))
print( Dictionary,'\n')


list1=[-1000, 500, -600, 700, 5000, -90000, -17500]
def is_positive(num):
    return num < 0
    negativeNumbers = list(filter(is_positive, map(abs, list1)))
    print(negativeNumbers)




