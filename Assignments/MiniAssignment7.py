#File Handling code
file = open("C:\\Users\\malpraneeth\\Downloads\\Pythonfilereading.txt", "r")
str = file.read()
sentence = str.split()
max_len = len(max(sentence, key=len))
for word in sentence:
    if len(word) == max_len:
        longest_word = word
print(longest_word)

#Error handling code
class FormulaError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def error():
    while True:
        string = input("enter string: ")
        if string != 'quit':
            lst = string.split(" ")
            length = len(lst)
            try:
                if length != 3:
                    raise FormulaError("String should contain 3 elements")
                elif lst[1] != '+' or lst[1] != '-':
                    raise FormulaError("String should contain '+' or '-' symbol")
            except FormulaError as e:
                print("formula error", e.data)
            except ValueError:
                print(ValueError.args)
            else:
                result = eval(string)
                print(result)
        else:
            break

error()

