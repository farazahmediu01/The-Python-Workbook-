favorite_numbers ={
    'faiq': 13,
    'faiez': 3,
    'faraz': 9,
    'sarab': 26,
    'sameer': 1,
    'ali': 1, 
}
favorite_numbers_list = [key for key in favorite_numbers]
favorite_numbers_list.append('naseer')
favorite_numbers_list.append('shoaib')
favorite_numbers_list.append('tanveer')


for key in favorite_numbers_list:
    message = f"Favorite number of {key} is {favorite_numbers.get(key)}."
    print(message)    
