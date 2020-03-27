'''
The counter function counts down from start to stop when start is bigger than stop,
and counts up from start to stop otherwise.
Fill in the blanks to make this work correctly.
'''
'''
def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"
'''

'''
def count_letters(text):
    result = {}
    # Go through each letter in the text
    for letter in text.lower():
        # Check if the letter needs to be counted or not
        if letter.isalpha():
            if letter in result:
                result[letter] = result[letter] + 1
            else:
                result[letter] = 1

            # Add or increment the value in the dictionary
        # if letter in result:
        # 	result[letter] = result[letter] + 1

    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}



'''
'''
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x == 0 :
				return_string += ","
			return x
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x == stop:
				return_string += ","
			return x
	return return_string
'''


# def car_listing(car_prices):
#     result = ""
#     for key, value in car_prices.items():
#         result += "{key} costs {value} dollars".format(key=key,value=value) + "\n"
#         # result += f"{key} cost {value} dollars\n"
#     return result


# print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
#                    "Ford Fiesta": 13000, "Toyota Prius": 24000}))

# def highlight_word(sentence, word):
# 	return sentence.replace(word,word.upper())

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


def format_address(address_string):
    # Declare variables
	home = ""
	street = ""
    # Separate the address string into parts
	# string[]
    # Traverse through the address parts
    # for space in range(2):
	index = address_string.find(" ")
	home = address_string[:index]
	street = address_string[index:]
    	# Determine if the address part is the
    	# house number or part of the street name

        # Does anything else need to be done
        # before returning the result?

        # Return the formatted string
	return "house number {home} on street named {street}".format(home=home,street=street)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
