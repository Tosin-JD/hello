print("Hello, world!")

content = str()
with open('file.txt') as file_handle:
    for line in file_handle:
        print(line)


