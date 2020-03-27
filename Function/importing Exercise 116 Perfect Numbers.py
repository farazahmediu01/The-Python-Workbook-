# import Exercise_116_Perfect_Numbers
# from Exercise_116_Perfect_Numbers import is_positive_integer as pi
# from Exercise_116_Perfect_Numbers import main as m
# a = Exercise_116_Perfect_Numbers.is_positive_integer(29)
# Exercise_116_Perfect_Numbers.main()

# print(pi(10))
# print(pi(6))
# print(pi(28))
# print(pi(496))
# print(pi(469))
# m(1000)
'''
The loop function is similar to range(),
but handles the parameters somewhat differently: 
it takes in 3 parameters: the starting point, the stopping point, and the increment step. 

When the starting point is greater than the stopping point, 
it forces the steps to be negative. 

When, instead, the starting point is less than the stopping point, 
it forces the step to be positive. 
Also, if the step is 0, it changes to 1 or -1. 

The result is returned as a one-line, space-separated string of numbers. 
For example, loop(11,2,3) should return 11 8 5 and loop(1,5,0) should return 1 2 3 4. 

Fill in the missing parts to make that happen.


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