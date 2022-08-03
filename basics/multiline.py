data = "" # empty string

while True:
    line = input("line >>> ")
    if not line:
        break
    data += line+" "

print("You have entered following data")
print(data)