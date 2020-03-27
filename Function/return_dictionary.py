def build_person(first_name, last_name, middle_name=''):
    if middle_name: INFO = {'first': first_name, 'middle': middle_name, 'last': last_name}
    else: INFO = {'first': first_name, 'last': last_name}

    return INFO


def print_info_in_sequence(sequence):
    for key in sequence.keys():
        print(f"\n{key} = {sequence[key]}")

def build_person_info(first, last, middle='', age=None):
    INFO = dict()
    if first : INFO['first'] = first
    if middle:INFO['middle'] = middle
    if last  :INFO['last'] = last
    if age   :INFO['age'] = age
    
    return INFO


# INFO = build_person('Jamil', 'Khan', 'Mashkoor Ahmed')
# print(INFO)

INFO = build_person_info('faraz', middle='ahmed', last='muslim', age=22)
print_info_in_sequence(INFO)
