total = 1

def localVar():
    def inside():
        print('Hello')

a = localVar()
a.inside()
