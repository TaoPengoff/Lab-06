# Tao Peng
# menu
def print_menu():
    print('Menu\n------------- \n1. Encode\n2. Decode\n3. Quit\n')
    option = input('Please enter an option: ')
    return option

# encode function
def encode(password):
    result = ''
    for i in password:
        current = int(i)
        current += 3
        if current > 9:
            current -= 10
        result += str(current)
    return result

# decode function
def decode(password):
    result = ''
    for i in password:
        current = int(i)
        current -= 3
        if current > 9:
            current += 10
        result += str(current)
    return result

if __name__ == '__main__':
    # default
    password = ''
    option = print_menu()
    password_stored = False
    type = ''
    while option != '3':
        # encode display
        if option == '1':
            if not password_stored or type != 'decode':
                password = input('Please enter your password to encode: ')
                password_stored = True
                print('Your password has been encoded and stored!\n')
                type = 'encode'
            else:
                print(f'The encoded password is {password}, and the original password is {decode(password)}.\n')
                password_stored = False
        # decode display
        elif option == '2':
            if not password_stored or type != 'encode':
                password = input('Please enter your password to decode: ')
                password_stored = True
                print('Your password has been decoded and stored!\n')
                type = 'decode'
            else:
                print(f'The encoded password is {encode(password)}, and the original password is {password}.\n')
                password_stored = False
        # new start
        option = print_menu()