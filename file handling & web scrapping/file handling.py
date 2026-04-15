# #1.first way :-
lst=["ali\n","mona\n","laila\n","salah\n"]

file = open(r"C:\Users\moham_f78sqay\Desktop\student info.txt","w")
file.write("welcome everybody\n")
file.write("welcome to college\n")
file.writelines(lst)
file.close() 

# W --> write (يمسح القديم ويكتب جديد)
# a --> append (يضيف على القديم)
#------------------------------------------------------------------------------------

#2.second way (مع with)
lstem = ("mmm\n","ggg\n","sss\n")

with open(r"C:\Users\moham_f78sqay\Desktop\employee.txt","w") as f:
    f.write("to check salary check your email\n")
    f.writelines(lstem)
