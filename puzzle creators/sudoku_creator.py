# function that intakes a nested array and returns a new array that first reverses the order
# of elements, and then capitalizes every other letter
# ['a', 'b', 'c', ['d', 'e', 'f'], 'g'] => ['C', 'b', 'A', ['f', 'E', 'd'], 'G']

def reverse_nested(arr : list, counter:int=0) -> list:
    narr = []
    for index in range(len(arr)):
        if isinstance(arr[index], list):
            temp = arr[index]
            temp.insert(0, 'a')
            narr.append(reverse_nested(arr[index]))[1:]
        else:
            if not (index+1) % 2:
                narr.append(arr[index].upper())
            else:
                narr.append(arr[index])
    return narr

print(reverse_nested(['a', 'b', 'c', ['d', 'e', 'f']]))