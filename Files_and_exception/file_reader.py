path_pi = r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Files_and_exception\pi_file'
path_txt = r'D:\Downloads\python\Python\Programs\visual studio code\Starting from Introduction\Files_and_exception\txt'


with open('txt') as file_handle:
    
    size_to_read = 10
    # for content in file_handle.read(size_to_read):
    content = 'abc'
    while len(content) > 0:    
        content = file_handle.read(10)
        print(content, end='*')

    
