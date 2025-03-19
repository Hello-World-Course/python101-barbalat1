
name = input("Hello, whats your name")
num_char_name= len(name)
if num_char_name < 2 :
    print('Your name is too short')
    name=None

user_input = input(f"{name}, please choose board size: ")

if user_input.isdigit():  # בדיקה שהקלט מספרי
    board_size = int(user_input)
    if not (0 <= board_size <= 26):  # עכשיו מקבל בין 0 ל-26
        print(f"{name}, you have entered an illegal board size")
        board_size = None
else:
    print(f"{name}, you have entered an illegal board size")
    board_size = None

if board_size is not None:  # רק אם גודל הלוח חוקי
    user_input1 = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")

    if user_input1.isdigit():
        number_of_mines = int(user_input1)
        max_mines = (board_size * board_size) // 2  # חצי מגודל הלוח

        if not (1 <= number_of_mines <= max_mines):  # מספר מוקשים חייב להיות בטווח
            print(f"{name}, you have entered an illegal number of mines")
            number_of_mines = None
    else:
        print(f"{name}, you have entered an illegal number of mines")
        number_of_mines = None





