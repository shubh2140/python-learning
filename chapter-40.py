dict = {
    "name": "Shubham",
    "age": 25,
}

print(dict.get("name"))
print(dict.get("names"))

duplDic = {
    "address": "Jabalpur",
     "age": 20,
}

dict.update(duplDic)
print(dict)