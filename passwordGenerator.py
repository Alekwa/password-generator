import random

caps_alph ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alph ="abcdefghijklmnopqrstuvwxyz"
special_char = "!@#$%^&*_?\/"
nums = "0987654321"

password = caps_alph + small_alph + special_char + nums

password_length = 8

password = "".join(random.sample(password, password_length))

print("Password is: " +password)

#Desktop Notification import timer from plyer import notification

#if name = "main":
 #   while True: notification.notify( title = "ALERT!!", message = "Take a break! It has been an hour!!", timeout = 10 )
   # time.sleep(3600)