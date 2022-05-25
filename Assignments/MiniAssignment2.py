#pascal code

def pascal(n):
    pascal_list = []
    for i in range(n):
        temp_list = []
        for j in range(n):
            if j == 0:
                temp_list.append(1)
            elif i==0:
                temp_list.append(0)
            else:
                temp_list.append(pascal_list[i-1][j]+pascal_list[i-1][j-1])
        pascal_list.append(temp_list)
    return pascal_list
number= int(input("enter number ="))
l = pascal(number)
print(l)
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=" ")
    print()

#Half diamond code



def pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            # printing space
            print(" ", end=" ")

        for j in range(i + 1):
            # printing star
            print("* ", end="")
        print()
    for i in range(n - 1):
        for j in range(i + 1):
            # printing space
            print(" ", end=" ")

        for j in range(n - i - 1):
            # printing star
            print("* ", end="")
        print()
# taking input
n = int(input('Enter the number of rows: '))
# calling function
pattern(n)

#hollow triangle


n = int(input('enter no of rows ='))
for i in range(1,n+1):
    for j in range(1,2*n):
        if i == n or i+j==n+1 or j-i == n-1:
            print('*',end="")
        else:
            print(end =" ")
    print()

#Reverse Hollow Pyramid
nrows= int(input("enter no of rows:"))

for row in range(1,nrows+1):
    for col in range(1,nrows+1):
        if(col == nrows) or (row == 1) or (col == row):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()



