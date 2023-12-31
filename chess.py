"""
Chess PGN Recorder

Author: Daniel Aguilar Darío
This program allows users to record and save chess games in PGN format.
"""


# Menu functions
def menu1():
    print("1. Create game")
    print("2. Information")
    print("3. Exit program")


def menu2():
    print("1. Record game moves")
    print("2. Add game information")
    print("3. Statistics")
    print("4. Add comments to moves")
    print("5. Create .PGN file")
    print("6. Return to main menu")


def tags():
    roster = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
    str_matrix = []

    for tag in roster:
        value = input(f"Enter the value for {tag}: ")
        str_matrix.append([tag, value])

    return str_matrix


def moves(game):
    move_number = 1
    terminations = ['#', '1/2-1/2', '*']

    while True:
        white_move = input(f"Move {move_number} White: ")

        if (not white_move or
                any(termination in white_move for
                    termination in terminations)):
            game.append((white_move,))
            break

        black_move = input(f"Move {move_number} Black: ")

        if any(termination in black_move for termination in terminations):
            game.append((white_move, black_move))
            break

        game.append((white_move, black_move))
        move_number += 1

    return game


def statistics(game):
    notations = {
        '+': 'Check',
        '#': 'Checkmate',
        '!': 'Good move',
        '!!': 'Excellent move',
        '?': 'Bad move',
        '??': 'Very bad move',
        '0-0': 'Short castling',
        '0-0-0': 'Long castling',
        'a.p': 'En passant capture'
    }

    white_statistics = {key: 0 for key in notations}
    black_statistics = {key: 0 for key in notations}

    for moves in game:
        for index, color_stats in enumerate([white_statistics,
                                             black_statistics]):
            if index < len(moves):
                move = moves[index]
                for notation, description in notations.items():
                    color_stats[notation] += move.count(notation)

    print("White's Statistics:")
    for notation, description in notations.items():
        print(f"{description}: {white_statistics[notation]}")

    print("\nBlack's Statistics:")
    for notation, description in notations.items():
        print(f"{description}: {black_statistics[notation]}")


def comments(game):
    move_num = int(input("Enter the move number you want to comment on: "))
    if move_num > len(game) or move_num <= 0:
        print("Invalid move number!")
        return

    color = input("Is the comment for white (w) or black (b)? ").lower()
    if color not in ['w', 'b']:
        print("Invalid color choice!")
        return

    comment = input("Write your comment: ")

    index = move_num - 1
    if color == 'w':
        move_with_comment = game[index][0] + " " + comment
        game[index] = (move_with_comment, game[index][1])
    else:
        if len(game[index]) == 2:
            move_with_comment = game[index][1] + " " + comment
            game[index] = (game[index][0], move_with_comment)
        else:
            print("There's no black move for this turn to comment on!")


def PGN(str_matrix, game):
    for tag, value in str_matrix:
        print(f"[{tag} \"{value}\"]")
    print()

    for index, (white, *black) in enumerate(game, start=1):
        print(f"{index}. {white} {' '.join(black)}", end=" ")
    print("\n")

    save_file = input("Do you want to save it as a\
                      .PGN file? (yes/no): ").lower()
    if save_file == 'yes':
        file_name = input("Enter the name for the file (without extension): ")
        with open(file_name + ".PGN", "w") as file:
            for tag, value in str_matrix:
                file.write(f"[{tag} \"{value}\"]\n")
            file.write("\n")

            for index, (white, *black) in enumerate(game, start=1):
                file.write(f"{index}. {white} {' '.join(black)} ")
            file.write("\n")
        print(f"PGN saved as {file_name}.PGN!")


def read_info():
    try:
        with open("info.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: info.txt file not found!")


def main():
    str_matrix = []
    game = []

    while True:
        menu1()
        choice1 = input("Choose an option: ").replace("png", "PNG")
        if choice1 == "1":
            while True:
                menu2()
                choice2 = input("Choose an option: ").replace("png", "PNG")
                if choice2 == "1":
                    moves(game)
                elif choice2 == "2":
                    str_matrix = tags()
                elif choice2 == "3":
                    statistics(game)
                elif choice2 == "4":
                    comments(game)
                elif choice2 == "5":
                    PGN(str_matrix, game)
                elif choice2 == "6":
                    break
                else:
                    print("Invalid option, try again.")
        elif choice1 == "2":
            read_info()
        elif choice1 == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option, try again.")


main()
