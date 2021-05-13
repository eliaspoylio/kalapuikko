import re

with open("testconf.txt","r") as f:
    data = f.read()
    lines = f.readlines()

found = re.findall(r"(?<={{)(.*?)(?=}})",data,re.M)

# remove duplicates
found = list(dict.fromkeys(found))

my_dict = {}

for key in found:
    x = input(key+':')
    my_dict[key]=x
print(my_dict)

for key, value in my_dict.items():
    pattern = '{{'+key+'}}'

    data = re.sub(pattern, value, data, flags = re.M)
print(data)