r'''
path_pi = r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Files_and_exception\pi_file'
path_txt = r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Files_and_exception\txt'
with open(path_pi) as file_handle:
    # lines = file_handle.readlines()

    # string = ''
    for line in file_handle:
    # string += line.rstrip()
        print(line)
# print(string)
# print(len(string))

# decimal_part = string[2:]
# print(f"Decimal part =  {decimal_part}\nlenght = {len(decimal_part)}")

# help(open(path_pi))
'''

from math import pi

