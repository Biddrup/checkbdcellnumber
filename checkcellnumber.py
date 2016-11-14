def isphonenumber(text):
    #The number should be 12 digit
    if len(text) != 12:
        return 'Cell number should be 10 digit'
    for i in range(0, 3):
        if not text[i].isdecimal():
            return 'First, 3 digit is only number'
    if text[3] != '-':
        return "Please, give a '-' after first three digit"
    for i in range(4, 7):
        if not text[i].isdecimal():
            return 'Second, 3 digit is only number'
    if text[7] != '-':
        return "Give a '-' after second 3 digits"
    for i in range(8, 12):
        if not text[i].isdecimal():
            return 'Last will be 4 digits'
    return 'You have putted a correct cell number'

#Will take a cell number from you
print('Please, give me a cell number with 10 digits (Ex-111-222-3333)')
user = input()

#Check the number via this
print(isphonenumber(user))
