number = input()

if number[0:3] == '880':
    for i in range(3, 13):
        if not number[i].isdecimal():
            print('This is not')
    else:
        print('Yes, this is')
else:
    print('How this one')
