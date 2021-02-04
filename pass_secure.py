SECURE = (('s', '$'), ('and','&'), ('a', '@'), ('o', '0'), ('i', '1'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__=='__main__':
    password = input('enter your password: ')
    password = securePassword(password)
    print('Your secure password is',password)
