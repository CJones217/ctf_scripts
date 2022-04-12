import json

f = open('words.json')

data = json.load(f)

print(len(data))

q = data[(105*4)%2236]
print(q)

