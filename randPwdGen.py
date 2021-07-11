import random as r
import re


print('Password types:\n\t1. Normal\n\t2. Sophisticated')
while True:

    pwdC = int(input('\nEnter your choice (1 or 2): '))
    if pwdC not in range(1,3):
        print('\nOnly enter 1 or 2')
        continue
    elif pwdC == 1:
        passlen = int(input("enter the length of password: "))
        chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        pwd =  "".join(r.sample(chars, passlen ))
        print (pwd)
        break
    elif pwdC == 2:

        def pwdGenr(sl, pl):
            rdm = []
            for e, p in zip(sl, pl):
                inp = r.sample(e, p)
                for i in inp:
                    rdm.append(i)
            r.shuffle(rdm)
            test = rdm[0]
            if re.match('[0-9 | !@#$%&*]', test):
                test = ''.join(rdm)
                res = re.search('[a-zA-Z]+?', test).start()
                rdm[0], rdm[res] = rdm[res], rdm[0]
            return ''.join(rdm)
        
        passlen = int(input("Choose the password length (8, 10, 12, 16): "))
        if passlen < 8: passlen = 8
        if passlen > 16: passlen = 16
        sampleList = ['abcdefghijklmnopqrstuvwxyz', '0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!@#$%&*']
        partitions = {8 : [2,2,2,2], 10 : [2,3,3,2], 12 : [4,3,3,2], 16 : [6,4,5,3]}
        
        print(f'The {passlen} length password is: {pwdGenr(sampleList, partitions[passlen])}')
    break
