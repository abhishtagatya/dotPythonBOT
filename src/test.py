usr = input()
usr_arg = usr.split()

cmd = ['check','key']

def check_arg(option=[]):

    if 'a' in option:
        print(option)
        print('Yes')
    else :
        print(option)
        print('Damn!')

if cmd[0] in usr:
    check_arg(usr_arg)
else :
    print('Failed')
