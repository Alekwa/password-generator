# password-generator
import random

caps_alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alphabet ="abcdefghijklmnopqrstuvwxyz"
special_character = "!@#$%^&*_?\/"
num = "0987654321"

password = caps_alph+small_alph+special_char+number

password_length = 8

password = "".join(random.sample(password, password_length))

print("Password is: " +password)


#Desktop Notification
import timer
from plyer import notification

if __name__ = "__main__":
  while True:
    notification.notify(
      title = "ALERT!!", 
      message = "Take a break! It has been an hour!!",
      timeout = 10
      )
      time.sleep(3600)
  
