import math

game_state = ["_" for i in range(0, 9)]


def print_board():
    dim = int(math.sqrt(len(game_state)))
    for i in range(0, dim):
        print(game_state[i*dim:(i+1)*dim])


def update_board(position, symbol):
    # Task: Check if the position is valid (0-8)
    if not 0<=position<=8 or not game_state[position] == "_":
        print("Invalid position")
        exit(1)
    # Task: Check if the position is empty
    # otherwise return with a invalid message to the user
    game_state[position] = symbol


def game_finished():
    # Write logic to decide if game is finished
    # and print the result ("win", "loose", "draw")
    dim = int(math.sqrt(len(game_state)))
    winning_combos = list()
    # rows
    for i in range(0, dim):
        tmp = list()
        for j in range(0, dim):
            tmp.append(i*dim+j)
        winning_combos.append(tmp)
    # columns
    for i in range(0, dim):
        tmp = list()
        for j in range(0, dim):
            tmp.append(dim*j+i)
        winning_combos.append(tmp)
    # diagonal top right to left bottom
    tmp = list()
    for i in range(0, dim):
        tmp.append(i+dim*i)
    winning_combos.append(tmp)
    tmp = list()
    for i in range(0, dim):
        tmp.append(dim-i-1+dim*i)
    winning_combos.append(tmp)
    for combo in winning_combos:
        winning = False
        symbol = game_state[combo[0]]
        for i in range(0, dim):
            if symbol == game_state[combo[i]] and symbol != "_":
                winning = True
            else:
                winning = False
                break
        if winning:
            print("Game Over. Player {} wins!".format(game_state[combo[0]]))
            exit(1)
    return False


if __name__ == "__main__":
    print("Welcome to TicTacToe!")
    dim = int(input("Choose a dimension for the baord: "))
    game_state = ["_" for i in range(0,dim*dim)]
    print("You can put your 'x' at the following positions:")
    fields = ""
    for x in range(0, dim):
        fields += "["
        for y in range(0, dim):
            fields += str(y+ x*dim)
            fields += ", "
        fields = fields.rsplit(", ", 1) [0]
        fields += "]\n"
    print(fields)

    print("Current board:")
    print_board()
    playing = "X"
    next_playing = "O"
    while not game_finished():
        i = int(input("Where do you want to put your '{}'? (0-{}): ".format(playing, dim*dim-1)))
        update_board(i, playing)
        # Task: implement the opponents move
        print_board()
        tmp = playing
        playing = next_playing
        next_playing = tmp
