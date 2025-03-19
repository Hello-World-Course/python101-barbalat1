# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
name = input("Hello, whats your name")
num_char_name= len(name)
if num_char_name < 2 :
    print('Your name is too short')
    name='None'

board_size = int(input(f"{name}, please choose board size"))
if 0 >= board_size or  board_size>=26:
    print(f"{name}, you have entered illegal board size")
    board_size='None'

user_input = (input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
if user_input.isdigit():
    number_of_mines = int(user_input)
    half_board_size = ((board_size * board_size) / 2)
    if 0 >= number_of_mines or number_of_mines >= half_board_size:
        print(f"{name}, you have entered illegal board size")
        number_of_mines = 'None'
else:
    print("Invalid input! Please enter a number.")


