"""That's my solution from problem 1"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    result_list = list()
    with open(path, mode='r', encoding='utf-8') as file:
        content = file.readlines()
    for line in content:
        result_list.append(line.strip())
    return result_list


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    visible_count = 1
    temp_highest = int(input_line[1])
    for building in input_line[2:-1]:
        if int(building) > temp_highest:
            visible_count += 1
            temp_highest = int(building)

    if visible_count == pivot:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', \
'*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    """
    for line in board:
        if '?' in line:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    flag = True
    for line in board[1:-1]:
        if len(line[1:-1]) != len(set(line[1:-1])):
            flag = False
    return flag


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', \
'*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if line[0] != '*' and not left_to_right_check(line, int(line[0])):
            return False
        elif line[-1] != '*' and not left_to_right_check(line[::-1], int(line[-1])):
            return False
    return True


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    """
    reversed_board = list()
    for i in range(len(board)):
        column = ''
        for elem in board:
            column += elem[i]
        reversed_board.append(column)

    if check_uniqueness_in_rows(reversed_board) and check_horizontal_visibility(reversed_board):
        return True
    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    if check_not_finished_board(board) and \
            check_horizontal_visibility(board) and \
            check_columns(board):
        return True
    return False


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
