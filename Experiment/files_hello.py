'''
link = "C:\\Users\\faraz\\Downloads\\abc.txt"

# with open(link) as file:

    # for line in file:
    #    print(line, end="")
    # print(file.closed)

    # inp = file.read()
    # index = inp.find('play')
    # for i in range(len(inp)):
    #    if i == index:
    #        print(inp)


# print(file.closed)
hello = "\u001b[31;1mfaraz \u001b[34;1mahmed"
print(hello)
'''
input_string = "Never Odd or Even"
new_string = ""
reverse_string = ""

# Traverse through each letter of the input string
for letter in input_string:
	# Add any non-blank letters to the
	# end of one string, and to the front
	# of the other string.
    if letter is not ' ':
        new_string += letter
        reverse_string = letter + reverse_string
    print("new_string",new_string)
    print("reverse_string",reverse_string,"\n")
