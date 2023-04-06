import tkinter as tk
from CellGrid import CellGrid
from AutomataRules import game_of_life_rules
from AutomataRules import update_cells
import time

#wipes a canvas and draws a new frame with the supplied elements
def draw_frame(cellGrid,c_width,c_height):
    canvas.delete("all")

    print(type(cellGrid))

    if cellGrid.grid == None:
        return
    
    universal_adj = 2

    for i,column in enumerate(cellGrid.grid):
        for j,cell in enumerate(column):
            cell_top_left = (i*(c_width/cell_grid.width) + universal_adj, j*(c_height/cell_grid.height) + universal_adj)
            cell_bottom_right = cell_top_left[0] + (c_width/cell_grid.width), cell_top_left[1] + (c_height/cell_grid.height)
            color = "black" 
            if cellGrid.grid[i][j] == 1:
                color = "white"
            canvas.create_rectangle(cell_top_left, cell_bottom_right, fill=color, outline="blue", width=1)


#setup
window = tk.Tk()
window.geometry("450x450")
window.title("Viewing Window")

#canvas
c_width = 400
c_height = 400
canvas = tk.Canvas(window, width=c_width+1, height=c_height+1, bg="grey")
canvas.pack()

#cell grid
cell_grid = CellGrid()

#draw frame
#draw_frame(cell_grid,c_width,c_height)
#window.update()

#loop
while True:
    time.sleep(.5)
    cell_grid = update_cells(cell_grid,game_of_life_rules)
    draw_frame(cell_grid,c_width,c_height)
    window.update()
    


#run
window.mainloop()