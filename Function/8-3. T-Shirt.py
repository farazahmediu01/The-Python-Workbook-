def make_shirt(size,message='all is well'):
    return f'Shirt size is {size}. \nShirt message is "{message.title()}. "'
var = make_shirt('small')

print(var)