import json 
#json.loads() --> json string --> dictt
#json.dumps() --> dict --> json string
data = {
    "students": [
        {
            "id": 1,
            "name": "Ali",
            "age": 22,
            "grade": 90,
            "city": "Cairo",
            "email": "ali@example.com"
        },
        {
            "id": 2,
            "name": "Mona",
            "age": 24,
            "grade": 85,
            "city": "Alex",
            "email": "mona@example.com"
        },
        {
            "id": 3,
            "name": "Omar",
            "age": 21,
            "grade": 95,
            "city": "Giza",
            "email": "omar@example.com"
        }
    ]
}

inform = json.dumps(data,indent=4) #json string 
#print(inform)



json_string = """
{
    "students": [
        {
            "id": 1,
            "name": "Ali",
            "age": 22,
            "grade": 90,
            "city": "Cairo",
            "email": "ali@example.com"
        },
        {
            "id": 2,
            "name": "Mona",
            "age": 24,
            "grade": 85,
            "city": "Alex",
            "email": "mona@example.com"
        },
        {
            "id": 3,
            "name": "Omar",
            "age": 21,
            "grade": 95,
            "city": "Giza",
            "email": "omar@example.com"
        }
    ]
}
"""
info = json.loads(json_string) #dict
for line in info["students"] :
    #print(line)
    del line["id"]#selete item
    #print(line)


#json.load() --> is used to read  json file ----> dict
with open(r"C:\Users\moham_f78sqay\Downloads\cars.json","r") as file :
    information = json.load(file)
    print(information)

i = {
"cities": [
    {
    "id": 1,
    "name": "Cairo",
    "country": "Egypt",
    "population": 9500000,
    "area_km2": 3085
    },
    {
    "id": 2,
    "name": "New York",
    "country": "USA",
    "population": 8419600,
    "area_km2": 783
    },
    {
    "id": 3,
    "name": "Tokyo",
    "country": "Japan",
    "population": 13960000,
    "area_km2": 2194
    },
    {
    "id": 4,
    "name": "Paris",
    "country": "France",
    "population": 2148000,
    "area_km2": 105
    }
        ]
}

#json.dump --> dict --> json file used to write

with open(r"C:\Users\moham_f78sqay\Downloads\sity.json","w") as f:
    data2 =json.dump(i,f,indent= 4)
    print(data2)