# Nick Greiner
# 10/17/24
# Lab 6 Version Control

# Display Menu
def display_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

# Get user's input
def get_user_input():
    user_input = input('Please enter an option: ')
    return user_input

# Encode user password
def encode(decoded_pass):
    pass_index = {0: '3',1: '4', 2: '5', 3: '6', 4: '7', 5: '8', 6: '9',
                  7: '0', 8: '1', 9: '2'}
    encodedStr =  ''
    for i in decoded_pass:
        encodedStr += pass_index[int(i)]

    return encodedStr

# Check user input
def validate_user_input(user_input, encoded_password = ''):
    if user_input == '1':
        decoded_pass = input('Please enter your password to encode: ')
        print("Your password has been encoded and stored!")
        encoded_pass = encode(decoded_pass)
        return encoded_pass
    if user_input == '2':
       print(encoded_password)
    if user_input == '3':
        exit()


# main loop
def main():
    encoded_pass = ''
    while True:
        display_menu()
        user_input = get_user_input()
        if user_input == '1':
            encoded_pass = validate_user_input(user_input)
        if user_input == '2':
           validate_user_input(user_input, encoded_password=encoded_pass)
if __name__ == '__main__':
    main()