keys = ['indus river', 'ravi', 'satlujh', 'liyari naddi', 'teri']
values = ['sindh', 'rawal pindi', 'bahawalpur', 'karachi', 'merbani']
data = dict(zip(keys, values))

print("\nFollowing are the names of few rivers and location where they flows:")
for key, value in data.items():
    message = f"The {key.title()} flows through {value.title()}."
    print(message)

print("\nThe name of few rivers are listed below:")
for key in data:
    print(key.title() + '.')

print("\nBlow are names of few cities famous by rivers flows through them:")
for value in data.values():
    print(value.title() + '.')


