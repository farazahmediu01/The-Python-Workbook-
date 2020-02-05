person = {
    'first_name': 'faraz',
    'last_name': 'ahmed',
    'age': '22',
    'city': 'karachi',
}

full_name = f"{person['first_name']} {person['last_name']}"
message_1 = f"Suspect = {full_name.title()}"
message_2 = f"Age = {person['age']}"
message_3 = f"Location = {person['city']}"

print(f"\n\n{message_1}\n{message_2}\n{message_3}")
