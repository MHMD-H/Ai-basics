import random
#random.seed(40) #the beginning of the start
num1 = random.randint(1,100)
print(num1) #59

#random.seed(40) #the beginning of the start
num2 = random.randint(1,100)
print(num2) #59 because we have the same seed

#random.seed(77) #the beginning of the start
num3 = random.randint(1,100)
print(num3) #33 because we changes the seed

#random.getstate--> used to store the state 
#random.setstate--> used to recall the state

state = random.getstate()
print(random.randint(1,100))#42
print(random.randint(1,100))#26 #every time we will get this numbers
random.setstate(state)
print(random.randint(1,100))#42
print(random.randint(1,100))#26

#detranbits() --> return numbers with bits
num4= random.getrandbits(8)#(0,255)
print(num4)

#random.randrange(start,end,step)
num5 = random.randrange(1,100,2)#just odd numbers
print(num5)


#--------------------------------------------------------------------------------------
#for lists and tuples

items = ["Egypt","france","italy","espain","UK","US"]

print(random.choice(items)) #choise randomly
print(random.choices(items,k=2)) #choose elemnts k=the number of elemnt(can ba repeat)
print(random.sample(items,k=2)) #choose elemnts k=the number of elemnt(cann't ba repeat)

random.shuffle(items)#rearrange the whole list
print(items)

#--------------------------------------------------------------------------------------
#for float

print("uniform(1, 5):", random.uniform(1, 5))
print("triangular(1, 10, 3):", random.triangular(1, 10, 3)) #focus on number 3