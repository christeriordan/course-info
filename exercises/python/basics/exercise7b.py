import json

keys = [1,2,3,4,5]
values = ["I","love","python","very","much"]
dict = {}

for key in keys:
    for val in values:
        dict[key] = val
        values.remove(val)
        break

with open('dict.json','w') as f:
    json.dump(dict,f)

with open('dict.json','r') as f:
    data = json.load(f)


