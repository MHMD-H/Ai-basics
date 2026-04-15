#in ----> is logical operator gives true/false

name = 'mohamed'
'e' in name

if 'ha' in name :
    print("i found it!")


    #open("file name") ---> to open file name
try: 
    count = 0
    file = open(r'C:\Users\moham_f78sqay\Documents\book mangement compresd[1]\book mangement\Application Files\book mangement_1_0_0_0\book mangement.deps.json.deploy')
    for line in file :
        line =line.strip()
        if not line.startswith("\"") :
           continue
        print(line.strip("\"")) 
        
except :
        print("i'm sorry!")


#range()---> return list of nymbers
print(list(range(4)))#[0, 1, 2, 3]


#We can create a new list by adding two existing lists together
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)#[1, 2, 3, 4, 5, 6]
print(a)# [1, 2, 3]


#sort(key = none,inverse = false) --> rearrange elements in list

nums=[5,44,13,78,4,9]
nums.sort()
print(nums)#[4, 5, 9, 13, 44, 78]
nums.sort(reverse = True)
print(nums)#[78, 44, 13, 9, 5, 4]


fruits = ['apples','strawberry','bananas']
fruits.sort()
print(fruits)#['apples', 'bananas', 'strawberry']
fruits.sort(reverse=True)#['strawberry', 'bananas', 'apples']
print(fruits)


#list.append()--> add elements in list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)#['book', 99]
stuff.append('cookie')
print(stuff)#['book', 99, 'cookie']