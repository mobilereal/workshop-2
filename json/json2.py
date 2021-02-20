import json

python_dict = {
    "name" : "Mobile & NN",
    "age" : 20
    "city" : "CM"
}

json_string = json.dumps(python_dict)

print(json_string)