def fixAny(original):
    # print('fixAny()')
    if(isinstance(original, list)):
        return [fixAny(i) for i in original]
    elif(isinstance(original, tuple)):
        return tuple(fixAny(i) for i in original)
    elif(isinstance(original, dict)):
        return fixDict(original)
    return original
    # print('End fixAny()')


def fixDict(original):
    # print('fixDict()')
    item = original.copy()
    check = False
    for k, v in item.items():
        # print('{0}: {1}'.format(k, v))
        if k is 'email':
            item[k] = 'redacted'
        elif k is 'password':
            check = True
        elif(isinstance(v, list) | isinstance(v, tuple) | isinstance(v, dict)):
            item[k] = fixAny(v)
    if check:
        del item['password']
    return item
    # print('End fixDict()')


value = {
    "email": "test@example.com",
    "password": "test",
    "user_info": {
        "name": "Test user",
        "email": {
            "email": "test@example.com",
            "password": "test",
            "user_info": {
                "name": "Test user",
                "email": "test@example.com"
            }
        },
        "tuple": (
            {
                "email": "cool",
                "password": "test",
                "check": "still"
            }, "bro")
    },
    "list": [
        {
            "email": "test@example.com",
            "password": "test",
            "user_info": {
                "name": "Test user",
                "email": "test@example.com"
            }
        }]
}

tofix = (value, value)

print(fixAny(tofix))
