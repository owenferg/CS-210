"""Flood-fill to count chambers in a cave.
CS 210 project.
Owen Ferguson, 10-24-2023
Credits: 
"""
import doctest
import cave
import config
import cave_view

GRAPHIC_DISPLAY = True  # Grid display using Tk
WIN_WIDTH = 300   # Width of graphical display in pixels
WIN_HEIGHT = 300  # Height of graphical display in pixels
TEXTUAL_DISPLAY = True  # Textual depiction of the cavern

def fill(cavern: list[list[str]], row_i: int, col_i: int):
    """Fill the whole chamber around cavern[row_i][col_i] with water
    """
    if row_i in range(len(cavern)) and col_i in range(len(cavern[row_i])) and cavern[row_i][col_i] == config.AIR:
        cavern[row_i][col_i] = config.WATER
        cave_view.fill_cell(row_i, col_i)
        fill(cavern, row_i - 1, col_i)
        fill(cavern, row_i + 1, col_i)
        fill(cavern, row_i, col_i - 1)
        fill(cavern, row_i, col_i + 1)
    else:
        return


def scan_cave(cavern: list[list[str]]) -> int:
    """Scan the cave for air pockets.  Return the number of
    air pockets encountered.

    >>> cavern_1 = cave.read_cave("data/tiny-cave.txt")
    >>> scan_cave(cavern_1)
    1
    >>> cavern_2 = cave.read_cave("data/cave.txt")
    >>> scan_cave(cavern_2)
    3
    """
    pocket_ct = 0

    for row_i in range(len(cavern)):
        for col_i in range(len(cavern[0])):
            if cavern[row_i][col_i] == config.AIR:
                fill(cavern, row_i, col_i)
                cave_view.change_water()
                pocket_ct += 1
                

    return pocket_ct

def main():
    doctest.testmod()
    cavern = cave.read_cave(config.CAVE_PATH)
    cave_view.display(cavern,config.WIN_WIDTH, config.WIN_HEIGHT)
    chambers = scan_cave(cavern)
    print(f"Found {chambers} chambers")
    cave_view.redisplay(cavern)
    cave_view.prompt_to_close()
    
if __name__ == "__main__":
    main()