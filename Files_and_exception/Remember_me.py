# We are creating a program that remember users name
import json

try:
    with open("user_name.json", "r") as file_handle:
        user_name = json.load(file_handle)
        print(f"Hello, {user_name}")

except:
    user_name = input("Enter your name and i will remeber you! ")
    with open("user_name.json", "w") as file_handle:
        json.dump(user_name, file_handle)
        print(f"Thank you {user_name} I will remember you.")

# Thats it
