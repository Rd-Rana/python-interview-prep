# fileObj = open("sample.txt")
# print(fileObj.read())

# with open("sample.txt") as fileObj:
#     print(fileObj.read())

# f = open("sample.txt")
# print(f.read(16))
# f.close()

with open("sample.txt") as f:
    for c in f:
        print(c)