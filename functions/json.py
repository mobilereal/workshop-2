import json

json_string = '{"name" : "Mobile & NN " ,"age" : 20, "city":"CH"}'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])