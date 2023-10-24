from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Create a copy of the input board only once
    board = input_board.copy()
    _flood_fill_recursive(board, old, new, x, y)
    return board

def _flood_fill_recursive(board: List[str], old: str, new: str, x: int, y: int) -> None:
    """The recursive helper function."""
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != old:
        return

    board[x] = board[x][:y] + new + board[x][y + 1:]

    _flood_fill_recursive(board, old, new, x + 1, y)  # D
    _flood_fill_recursive(board, old, new, x - 1, y)  # U
    _flood_fill_recursive(board, old, new, x, y + 1)  # R
    _flood_fill_recursive(board, old, new, x, y - 1)  # L


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
print('\n')

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....


# Add test case
modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=2)

for a in modified_board:
    print(a)
    
# Expected output:
# ~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~##########~~~~~~
# ~~~~~~#........#~~~~~~
# ~~~~~~#........#~~~~~~
# ~~~~~~#........#####~~
# ~~~~###............#~~
# ~~~~#............###~~
# ~~~~##############~~~~
