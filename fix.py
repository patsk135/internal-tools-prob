from mocks import *


def fixAny(x):
    if(isinstance(x, list) | isinstance(x, tuple)):
        for i in x:
            fixAny(i)
    elif(isinstance(x, dict)):
        fixDict(x)


def fixDict(x):
    # print("fixDict()")
    check = False
    for i in x:
        print(i)
        if(isinstance(value.get(i), dict)):
            fixDict(x.get(i))
        if i is "email":
            x[i] = "redacted"
        if i is "password":
            check = True
    if check:
        del x["password"]
    # print('End fixDict()')


fixAny(value)

print(value)
