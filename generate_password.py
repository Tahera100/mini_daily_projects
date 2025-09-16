import random 
import string

password = list(random.choices(string.punctuation, k=2) + 
                random.choices(string.ascii_letters + string.digits, k=10))
random.shuffle(password)
password = ''.join(password)
print(password)

