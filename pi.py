#Type 'python nameofthefile.py generate' in python shell to start this little project

import math, sys

class liczbaPi():

    if len(sys.argv) == 2:
        command = sys.argv[1]
        if command == 'generate':
            try:
                liczba = int(input('Enter a number of decimal places u want to have in your pi number. Maximum is 48.\n'))
                if liczba >= 0 and liczba <=48:
                    print('{:.{}f}'.format(math.pi, liczba))
                elif liczba > 48:
                    print('Your number should be lower then 49.')
                else:
                    print('Your number should be a positive integer.')
            except ValueError as error:
                    print('Make sure u are typing an integer.')