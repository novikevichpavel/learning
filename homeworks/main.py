with open("test.txt", "w") as new_file:  
    new_file.write("This is the first line in this test file\n")

with open("test.txt", "a") as new_file:  
    new_file.write("This is the second line in this test file\n")

with open("test.txt") as new_file:
    lines = new_file.readline()
    for line in lines:
        print(line)




