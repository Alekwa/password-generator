# password-generator
import random

caps_alph ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_alph ="abcdefghijklmnopqrstuvwxyz"
special_char = "!@#$%^&*_?\/"
number = "0987654321"

password = caps_alph+small_alph+special_char+number

password_length = 8

password = "".join(random.sample(password, password_length))

print("Password is: " +password)
