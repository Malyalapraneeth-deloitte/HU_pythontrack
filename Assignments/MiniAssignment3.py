# count duplicates in list
from collections import Counter
def duplicateCount(array):
    for element in array:
        dictionary = Counter(element)
        for keyvalue in dictionary:
            if dictionary[keyvalue] > 1:
                print(keyvalue, "--->", dictionary[keyvalue])
list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 4]]
print("It wll returns all the duplicate values from list of array list ")
duplicateCount(list)



#Merging two lists
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output_list = []
for i in range(len(list2)):
    for j in range(len(list1)):
        s = list1[i]+list2[j]
        output_list.append(s)
print(output_list,'\n')



#adding subList to list
nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
nested_list[2][1][2].extend(sub_list)
print(nested_list,'\n')



#Merging two dictionaries
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3,'\n')



#Renaming Key in dictionary
sampleDict ={ "name": "Kelly", "age": 25,"salary": 8000,   "city": "New york"}
sampleDict["location"] = sampleDict.pop("city")
print(sampleDict,'\n')



# Convert Dictionary to list
Dict = {"HuEx": [1, 3, 4],  "is": [7, 6],  "best": [4, 5]  }
resultList = []
for key in Dict:
    temp_list = []
    temp_list.append(key)
    for i in Dict[key]:
        temp_list.append(i)
    resultList.append(temp_list)
print(resultList)






