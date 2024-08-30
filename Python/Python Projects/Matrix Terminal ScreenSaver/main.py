# Matrix Visual Wallpaper

import shutil, random, sys, time
# shutil allows operation of a file
# sys provides functions and variables that allow user to work with python runtime environment or directly interact with intrepreter

MIN_STREAM_LENGTH = 6  # minimum 6 digits in a vertical stream
MAX_STREAM_LENGTH = 14 # Maximum 14 digits in a vertical stream


PAUSE = 0.1 # pause between each row of digits

STREAM_CHARS = ['0', '1'] # Characters appear on the sream

DENSITY = 0.01 # Desnsity ranges from 0 to 1.0

# finding and setting the size of the treminal window. 0 is width.
WIDTH  = shutil.get_terminal_size()[0]
WIDTH -= 1
# width -= 1 helps maintaing the terminal behaviou else trminal behaves differently

print("Digital Stream   --    Matrix")
print("Press Ctrl+C to quit.\n")
time.sleep(2) # pausing at the start

# creating a list of ints, one int for one column in the terminal window
# if int is 0, no character is printed
#int for a column in greater then 0, we print the charcter
columns = [0] * WIDTH
try:
    # print("debug: ", columns)
    #  print(len(columns))
    while True: 
        # setting up the counter for each column
        for i in range(WIDTH):
            if columns[i] == 0:
                # setting up the 0 column to a number less then 0 as per density 
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            # display a stream character if the column len is > 0
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='') # print a random stream character

                columns[i] -= 1 # Decreasing the column to 0
            else:
                print(' ', end="")
            
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
        # print(columns)
        # input("Press enter to continue")
except KeyboardInterrupt:
    sys.exit() # ctrl C will not show keyboard error. will just exit.





             

