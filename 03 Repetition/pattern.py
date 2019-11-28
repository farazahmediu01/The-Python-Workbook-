increment_variable = 0

for i in range(9):
    if i <= 4:
        increment_variable += 1
    
    if i >= 5:
        increment_variable -= 1
    print("*" * increment_variable)
    

'''
       * 
      ***  
     ******   
  ************
  ************************
  '''