import re

with open("testconf.txt","r") as f:
    data = f.read()

templates = re.findall(r"(?<={{)(.*?)(?=}})",data,re.M)

# remove duplicates
templates = list(dict.fromkeys(templates))

user_input = {}

for key in templates:
    x = input(key+':')
    user_input[key]=x
print("##########################")

for key, value in user_input.items():
    pattern = '{{'+key+'}}'

    data = re.sub(pattern, value, data, flags = re.M)
print(data)