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

fruits.sort(reverse=True)
print(fruits)



#dict.items()--> define list of tuple



file = open(r'C:\Users\moham_f78sqay\Downloads\mbox-short.txt')

countEmail = {}
countDomain = {}
countTime = {}


for line in file:
    inform = line.split()
    
    f_time = line.find(":")
    time = line[f_time-2:f_time]

    email =inform[1]

    f_domain = email.find('@')
    domain = email[f_domain+1:]

    countEmail[email] = countEmail.get(email,0) +1
    countDomain[domain] = countDomain.get(domain,0) +1
    countTime[time] = countTime.get(time,0) +1
    
lemail =[]
for ke,ve in countEmail.items() :
        lemail.append((ve,ke))
lemail.sort(reverse=True)
for ke,ve in lemail :
      print(ve,ke)


ldomain = []
for kd,vd in sorted(countDomain.items()) :
      print(vd,kd)

ltime =[]
for kt ,vt in countTime.items() :
      ltime.append((vt,kt))

ltime.sort(reverse = True)
for ve,ke in ltime :
      print(ve,ke)
