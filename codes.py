import random
chars = '_01234567890qwertyuiopasdfghjklzxcvbnm'

def getCode():
    code = ''
    for x in range(5):
        i = random.randint(0,35)
        code += chars[i]
    return code.upper()