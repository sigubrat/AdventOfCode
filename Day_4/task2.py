draw = []
boards = []
drawn_boards = []

    
def parse_input(file):
    """
    Parses this day's input data. 
    The first line will contain a random sequence of numbers. 
    After that, matrices of random numbers will follow, separated by a blank line. 
    """
    with open(file, "r") as fp: 
        # Get the first line and parse it into a global list of integers
        nums = fp.readline()
        draw[:] = [int(x) for x in nums.split(",")]
        # Now we need to go through the rest and get each matrix
        lines = fp.readlines()
        
        cur_board = []
        copy = []
        for line in lines:
            if line.isspace():
                if cur_board:
                    boards.append(cur_board)
                    drawn_boards.append(copy)
                cur_board = []
                copy = []
                continue

            line = line.strip()
            line = line.replace("  ", " ")
            row = [int(x) for x in line.split(" ")]
            copy_row = [False for x in row]
            cur_board.append(row)
            copy.append(copy_row)

        boards.append(cur_board)
        drawn_boards.append(copy)

def update_drawn_boards(number):
    # Loop through all the boards
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, n in enumerate(row):
                # Check if the number is the same
                if n == number:
                    drawn_boards[i][j][k] = True

def check_for_winner(board):
    """
    Searches through the boards and returns the id of the board if anyone has a full row or a full column. 
    If no winner were found, it returns -1. 
    """
    # First check if someone has a full row
    count = 5
    for j, row in enumerate(board):
        for k, n in enumerate(row):
            if n is True:
                count-= 1
        if count < 1:
            return True
        else: 
            count = 5
    
    # If not, check if anyone has a full collumn
    count = 5
    for j in range(5):
        for k in range(5):
            if board[k][j] is True:
                count -=1
        if count < 1:
            return True
        else:
            count = 5
    # If no winner was found, return -1
    return False

def calculate_score(id, num):
    """
    Returns sum of all unmarked values in the provided board
    """
    score = 0
    for i, row in enumerate(drawn_boards[id]):
            for j, n in enumerate(row):
                if n is False:
                    score += boards[id][i][j]
    return score * num


def main():
    parse_input("data.txt")
    last_winner = 0
    winners = [False] * len(boards)
    # Loop through the drawn numbers
    for round, num in enumerate(draw):
        # Check if anyone has gotten that number
        update_drawn_boards(num)

        # No point checking before 5 numbers have been drawn
        if round >= 4:
            # Check each board if they've won
            for i, board in enumerate(boards):
                if check_for_winner(drawn_boards[i]):
                    winners[i] = True
                    score = calculate_score(i, num)
                    if winners.count(True) == len(boards):
                        print("Score: ", score) 
                        return 
                    

if __name__ == "__main__":
    main()