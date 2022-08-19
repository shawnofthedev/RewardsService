import string
import random

class RandomSeach():

    def generate_string():
        all_char = string.ascii_letters + string.punctuation + string.digits
        randomString = "".join(random.choice(all_char) for x in range(10))
        return randomString
