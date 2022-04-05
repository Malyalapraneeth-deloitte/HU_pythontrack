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
# takeing input
n = int(input('Enter the number of rows: '))
# calling function
pattern(n)



#printing Triangle



def pattern(n):
   for i in range(1, n+1):
      for j in range(0, i):
         # printing space
         print(" ", end=" ")

      for j in range(1, (n*2 - (2*i-1)) + 1):
         if i == 1 or j == 1 or j ==(n*2 -(2*i-1)):
            # printing star
            print("*", end=" ")
         else:
            # printing space
            print(" ", end=" ")
      print()

# taking input
n = int(input('Enter the number of rows: '))

# calling function
pattern(n)

