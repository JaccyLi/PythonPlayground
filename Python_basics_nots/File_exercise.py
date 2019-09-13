# e1
with open('../test_file/test_file1.txt') as trans:
    xl = trans.read()
    #print(xl)

# e2
with open('../test_file/how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# e3
with open('../test_file/how_many_lines.txt') as first_line_doc:
    first_line = first_line_doc.readline()
    print(first_line)

# e4
with open('../test_file/bad_bands.txt', 'w') as bad_bands_doc:
    bad_bands_doc.write("Flower")
with open('../test_file/bad_bands.txt') as bad_bands:
    d = bad_bands.read()
    print(d)

# e5
with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.write("Air Buddy")

