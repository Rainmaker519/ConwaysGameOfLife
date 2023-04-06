from CellGrid import CellGrid

def get_adjacent_cell(cell_loc,direction):
    new_cell_loc = None
    if direction == "up":
        new_cell_loc = [cell_loc[0], cell_loc[1] - 1]
    if direction == "down":
        new_cell_loc = [cell_loc[0], cell_loc[1] + 1]
    if direction == "left":
        new_cell_loc = [cell_loc[0] - 1, cell_loc[1]]
    if direction == "right":
        new_cell_loc = [cell_loc[0] + 1, cell_loc[1]]
    if direction == "up_left":
        new_cell_loc = [cell_loc[0] - 1, cell_loc[1] - 1]
    if direction == "up_right":
        new_cell_loc = [cell_loc[0] + 1, cell_loc[1] - 1]
    if direction == "down_left":
        new_cell_loc = [cell_loc[0] - 1, cell_loc[1] + 1]
    if direction == "down_right":
        new_cell_loc = [cell_loc[0] + 1, cell_loc[1] + 1]

    return new_cell_loc

def game_of_life_rules(cells,cell_loc):
    #print(cells)
    #get the state of the cell
    cell_state = cells[cell_loc[0]][cell_loc[1]]

    if cell_state == None:
        return None

    #get the state of the adjacent cells
    adjacent_cells = []
    for direction in ["up","down","left","right","up_left","up_right","down_left","down_right"]:
        a_cell_loc = get_adjacent_cell(cell_loc,direction)
        if a_cell_loc[0] < 0:
            a_cell_loc[0]  = a_cell_loc[0] + len(cells[0])
        if a_cell_loc[0] >= len(cells[0]):
            a_cell_loc[0] = a_cell_loc[0] - len(cells[0])
        if a_cell_loc[1] < 0:
            a_cell_loc[1] = a_cell_loc[1] + len(cells)
        if a_cell_loc[1] >= len(cells):
            a_cell_loc[1] = a_cell_loc[1] - len(cells)

        a_cell_val = cells[a_cell_loc[0]][a_cell_loc[1]]

        
        if a_cell_val >= 1:
            adjacent_cells.append(1)
        else:
            adjacent_cells.append(0)

    #count the number of adjacent cells that are alive
    alive_count = 0
    for cell in adjacent_cells:
        if cell == 1:
            alive_count += 1
    
    print(f"cell {cell_loc} has {alive_count} cells alive next to it.")
    print()

    #apply the rules
    if cell_state == 1:
        if alive_count < 2:
            return 0
        if alive_count == 2 or alive_count == 3:
            return 1
        if alive_count > 3:
            return 0
    if cell_state == 0:
        if alive_count == 3:
            return 1
        else:
            return 0


def update_cells(cells,rule):
    ref_cells = cells.grid
    new_grid = [[None for _ in range(cells.height)] for _ in range(cells.width)]
    #filter is a list, ordered from top left to bottom right going by rows
    for j in range(cells.height):
        for i in range(cells.width):
            #across each row left to right, then goes down to the next row
            new_grid[i][j] = rule(ref_cells,(i,j))
    new_cells = CellGrid(new_grid)
    return new_cells



def main():
    update_cells(CellGrid(),game_of_life_rules)

if __name__ == "__main__":
    main()
        