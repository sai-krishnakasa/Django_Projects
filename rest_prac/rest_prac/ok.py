def decor(func):
    def inner(*args,**kwargs):
        if 0 in args:
            print("can't use Zero")
        else:
            func(*args,**kwargs)

    return inner

@decor
def div(a,b):
    print(a%b)

div(5,0)

