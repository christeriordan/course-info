file = open('my_file.txt','r')

firstline = file.readline()
print("First line is: ",firstline)



text = file.read()
words = text.split()
print("Number of words: ", len(words), "\n")



line_count = 0

for line in file:
    if line != "\n":
        line_count += 1

file.close()

print("Number of lines: ", line_count)
