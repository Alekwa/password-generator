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
