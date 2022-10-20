# Python program to read
# json file


import json

# Opening JSON file
f = open('sample.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
"""listt=list()
listt=[i.keys() for i in data['bank_account']]
for i in data['bank_account']:
    print(i.keys())
print(listt)
print(data['bank_account'][0]['83389739'])"""
for i in data['bank_account']:
    for j in i:
        if "83389739" in j:
            print(i["83389739"]["password"])
            print("Yes, 'model' is one of the keys in the thisdict dictionary")
        else:
            print('not found')
# Closing file
f.close()
