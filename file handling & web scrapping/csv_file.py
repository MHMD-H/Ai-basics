import csv
#reading
path = r"C:\Users\moham_f78sqay\Downloads\data.csv"
data = []
with open(path,"r",newline= "") as file :
    #reader = csv.reader(file) #read as list
    reader = csv.DictReader(file) #read as dictionary
    
    for line in reader :
        print(line)
        data.append(line)
    

#overwrite
with open(r"C:\Users\moham_f78sqay\Downloads\edit_data.csv","w",newline="") as w_file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(w_file,fieldnames= fieldnames,delimiter= "-")
    writer.writeheader()
    writer.writerows(data)
        

#writing
new_data = [
    {"id":1, "name":"Ali", "age":22, "grade":90, "city":"Cairo", "email":"ali1@example.com", "phone":"01000000001"},
    {"id":2, "name":"Mona", "age":25, "grade":85, "cirty":"Alex", "email":"mona2@example.com", "phone":"01000000002"}
]

with open("C:\Users\moham_f78sqay\Downloads\student.csv","w",newline="") as file :
    fieldnames = ["id","name","age","grade","city","email","phone"]
    writer1 = csv.DictWriter(file,fieldnames=fieldnames) # write in this file
    writer1.writeheader()#set the headers
    writer1.writerows(new_data)#write data in the file

with open(r"C:\Users\moham_f78sqay\Downloads\student.csv","r",newline="") as file :
    reader_it = csv.DictReader(file)     
    for line in reader_it:
        print(line["name"])





