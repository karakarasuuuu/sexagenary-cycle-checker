from database import heavenly, earthly

def suffix(i: int) -> str:
    
    if i > 10 and i < 20: return 'th'

    t = i % 10
       
    if t == 1: return 'st'
    elif t == 2: return 'nd'
    elif t == 3: return 'rd'
    else: return 'th'

def validate(s: str) -> (bool, int):

    try:

        # + 1 part is to adjust the index
        h = heavenly.index(s[0]) + 1
        e = earthly.index(s[1]) + 1

    except ValueError: return False, -1

    # It is 61 instead of 60 because 60 is valid as well
    for i in range(h, 61, 10):
        
        # Use 12 to replace 0
        t = i % 12 if i % 12 != 0 else 12

        if t == e: return True, i

    return False, -1


if __name__ == '__main__':
    
    # testcase = []
    # for h in heavenly:
    #     for e in earthly:
    #         testcase.append(h + e)

    s = input('Please enter your question: ').strip()
    
    if len(s) != 2: print('Invalid input!')
    
    else: 

        result, index = validate(s)

        if result:

            print('Valid!')
            print('It is the ' + str(index) + suffix(index) + ' year!')

        else: print('It is not a valid year!')
