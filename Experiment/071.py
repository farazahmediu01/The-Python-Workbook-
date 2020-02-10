subjects = ['math', 'sst', 'physics', 'islamiat', 'urdu', 'programming', 'english']
for subject in subjects:
    print(subject.title())

inp = input("\nName the subject you hate most in list shown above: ")
subjects.remove(inp)

for subject in subjects:
    print(subject.title())