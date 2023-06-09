import math
import random
class CellGrid:
    def __init__(self,grid=None) -> None:
        self.random_start = False
        self.cell_view_size = 10
        self.width = 10
        self.height = 10
        self.off_state = 0
        self.off_color = "black"
        self.on_state = 1
        self.on_color = "white"
        self.outline_color = "black"
        self.outline_width = 1
        if grid == None:
            self.grid = self.create_grid()
        else:
            self.grid = grid

    def create_grid(self):
        grid = []
        for i in range(self.width):
            grid.append([])
            for j in range(self.height):
                if not self.random_start:
                    grid[i].append(self.off_state)
                else:
                    grid[i].append(math.floor(random.random() * 2))
        return grid

    
    
def main():
    cell_grid = CellGrid()
    print(cell_grid.grid[0][0])

if __name__ == "__main__":
    main()
    