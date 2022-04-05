import collections
class StringClass:
    def __init__(self,):
        self.string = input("enter the string: ")

    def length(self):
        return len(self.string)

    def listOfCharacters(self,s1):
        self.s1=s1
        return list(self.s1)


class PairsPossible(StringClass):
    def __init__(self,str_pair):
        self.str_pair = str_pair

    def pairsList(self):
        str_list = list(self.str_pair)
        pairsList = []
        for i in range(len(str_list)):
            for j in range(len(str_list)):
                pairsList.append([str_list[i], str_list[j]])

    def displayPairs(self):
        for pairs in self.pairsList():
            print(pairs, end=" ")


class SearchCommonElements(PairsPossible):
    def __init__(self):
        self.arr1 = collections(list(self.s1))
        self.arr2 =collections(list(self.str_pair))

    def common(self):
        commonElements = dict(self.arr1.items()&self.arr2.items())
        res=[]
        for (key,val) in commonElements.items():
            for i in range(0, val):
                res.append(key)
        return res
class EqualSumPairs(SearchCommonElements):

    def count(self):
        list = PairsPossible.pairsList()
        res=[]
        for pair in list:
            Sum = 0
            for j in range(len(pair)):
                Sum = Sum + int(pair[j])
            if Sum not in res:
                res.append(Sum)
        print("count of total number of pairs which has sum which is not equal to other pairs:",len(res))

    def displaySearchCommon(self):
        display_list = SearchCommonElements.common()
        print("result of searchCommonElements class:", display_list)


stringObj = StringClass('789')
stringlength = stringObj.length()
chars_list = stringObj.listOfCharacters('789')
print("length of String:",stringlength)
print("list of characters:",chars_list)

pair_obj = PairsPossible('890')
pair_obj.displayPairs()
sumPairObj = EqualSumPairs('890')
sumPairObj.count()
sumPairObj.displaySearchCommon()