import json

test_dict = {
    "hello" : 1,
    "bye" : 2
}

s = json.dumps(test_dict)

print(s)
print(json.loads(s))