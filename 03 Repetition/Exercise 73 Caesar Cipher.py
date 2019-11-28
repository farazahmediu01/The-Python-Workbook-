"Monitor lazerd"
#str.isspace()

text                  = input("Enter messge: ")
Shifted_value         = int(input("Enter the number you want to shift the value: "))

alphabet_lower        = "abcdefghijklmnopqrstuvwxyzabc"
alphabet_upper        = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC"
index                 = 0
loc_index_alph        = 0
increpted_text        = ""
repeted_value         = ""

for each_letter in text:

    if each_letter in alphabet_lower:
                      
            loc_index_alph = alphabet_lower.find(each_letter)            
            increpted_text += text[index].replace(text[index],alphabet_lower[loc_index_alph + Shifted_value])

    elif each_letter in alphabet_upper:        
            loc_index_alph = alphabet_upper.find(each_letter)            
            increpted_text += text[index].replace(text[index],alphabet_upper[loc_index_alph + Shifted_value])        
    
    elif each_letter == " ":
        increpted_text += "_"
    
    elif each_letter.isnumeric:
        try:
            increpted_text += str(int(each_letter) + Shifted_value)
        except:
            increpted_text += each_letter
    
    else:
        increpted_text += each_letter           
        
    repeted_value += each_letter
    
    index = 1


print('increpted_text =',increpted_text)