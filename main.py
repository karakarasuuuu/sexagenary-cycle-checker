from database import heavenly, earthly

def suffix(i: int) -> str:
    
    if i > 10 and i < 20: return 'th'

    t = i % 10
       
    if t == 1: return 'st'
    elif t == 2: return 'nd'
    elif t == 3: return 'rd'
    else: return 'th'

if __name__ == '__main__':

    testcase = []
    for h in heavenly:
        for e in earthly:
            testcase.append(h + e)

    print(len(testcase))

    valid = 0

    for string in testcase:
    
        try:
            
            # + 1 part is to adjust the index 
            h = heavenly.index(string[0]) + 1
            e = earthly.index(string[1]) + 1
        
        except ValueError: print('Invalid input!')

        done = False

        for i in range(h, 61, 10):

            t = i % 12 if i % 12 != 0 else 12

            if t == e: 

                print('Valid!')
                print('It is the ' + str(i) + suffix(i) + ' year!')
                print(string)
                done = True
                valid += 1
                
                break

        # if not done: print('It is not a valid year!')

    print(valid)