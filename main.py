from database import heavenly, earthly

if __name__ == '__main__':

    string = input('Please enter your question: ')
    
    if len(string) != 2: print('Invalid input!')
    
    else:

        try:

            h = heavenly.index(string[0])
            e = earthly.index(string[1])
        
        except ValueError: print('Invalid input!')

        
