import bcrypt
import random
import string
import sys

class CommonManager():
    @staticmethod
    def compute_hash(text):
        encoded_text = text.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_text = bcrypt.hashpw(encoded_text, salt)
        return hashed_text.decode('utf-8')


    @staticmethod
    def check_hash(text, hashed_text):
        print(hashed_text, file=sys.stderr)
        return bcrypt.checkpw(text.encode('utf-8'), hashed_text.encode('utf-8'))


    @staticmethod
    def gen_hash(length=10):
        candidates = string.ascii_letters + string.digits
        return ''.join(random.choice(candidates) for _ in range(length))


common_manager = CommonManager()