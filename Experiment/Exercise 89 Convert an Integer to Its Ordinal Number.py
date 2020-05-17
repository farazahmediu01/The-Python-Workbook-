# ordinal numbers are the numbers written in natural language.
# ie: for integer '1' the ordinal numbers is 'one'.
# ie: for integer '2' the ordinal numbers is 'two'.


def int_to_ordinal(integer, ORDINAL):
    '''This function convert integer to its ordinal number.'''
    for ordinal in ORDINAL:
        if ordinal == integer:
            print('...')
            return ORDINAL[ordinal]
    print('!!!')
    return ' '


def main():
    ORDINAL = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
    }
    # for ordinal in ORDINAL:
    #     print(ORDINAL[ordinal])
    
    print('Enter an integer.')
    integer = int(input('> '))
    result = int_to_ordinal(integer, ORDINAL)
    print('Result =', result)

if __name__ == '__main__':
    main()