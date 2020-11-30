from database import heavenly, earthly

def suffix(i: int) -> str:
    
    if i > 10 and i < 20: return 'th'

    t = i % 10
       
    if t == 1: return 'st'
    elif t == 2: return 'nd'
    elif t == 3: return 'rd'
    else: return 'nd'

if __name__ == '__main__':

    string = input('Please enter your question: ').strip()
    
    if len(string) != 2: print('Invalid input!')
    
    else:

        try:

            # + 1 part is to adjust the index 
            h = heavenly.index(string[0]) + 1
            e = earthly.index(string[1]) + 1
        
        except ValueError: print('Invalid input!')

        done = False

        for i in range(h, 60, 10):

            if i % 12 == e: 

                print('Valid!')
                print('It is the ' + str(i) + suffix(i) + ' year!')
                done = True
                
                break

        if not done: print('It is not a valid year!')
