'''
1) Fill in the blanks of this code to print out the numbers 1 through 7.

'''

number = 1
while number <= 7:
	print(number, end=" ")
	number += 1

'''
2)The show_letters function should print out each letter of a word on a separate line. Fill in the blanks to make that happen.
'''

def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter

'''
3)Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
'''

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while n:
		count += 1
		n = n // 10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

'''
4) This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:
1 2 3

2 4 6

3 6 9

'''

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

'''
5)The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.
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
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

'''
6)The loop function is similar to range(), but handles the parameters somewhat differently: it takes in 3 parameters: the starting point, the stopping point, and the increment step. When the starting point is greater than the stopping point, it forces the steps to be negative. When, instead, the starting point is less than the stopping point, it forces the step to be positive. Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated string of numbers. For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. Fill in the missing parts to make that happen.

'''
def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step = 1
	if start > stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start,stop,step):
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty

