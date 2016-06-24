import time
import hashlib
import random
import sys
from requests import get

def gen_secret_key():
    return hashlib.md5(str(round(time.time() * 1000)).encode()).hexdigest()

def gen_session_val():
    ip = get('https://api.ipify.org').text
    current_time = round(time.time() * 1000)
    prng = random.randint(0, sys.maxint+1)
    return hashlib.md5(str(str(ip)+str(current_time)+str(prng)).encode()).hexdigest()