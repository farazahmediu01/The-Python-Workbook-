def describe_pet(pet_name, animal_type="dog", greeting='Hi'):
    print(f'\n{greeting}, Everyone how its going?')
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet('Millie','Cow','Hello')