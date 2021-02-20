import json

json_string = '{"name" : "Mobile & NN " ,"age" : 20,
 "city":"CM"}'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])