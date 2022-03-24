# llist = {"hello":1, "how":2,  "are":3, "you?":4}



line = "                                                             \n"
line = line.rstrip("\n").split()
line = ' '.join(line)



file = open("demo.txt", 'w')

file.write(line)

file.close()