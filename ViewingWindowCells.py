import tkinter as tk
from CellGrid import CellGrid
from AutomataRules import game_of_life_rules
from AutomataRules import update_cells
import time
import math




#wipes a canvas and draws a new frame with the supplied elements
def draw_frame(cellGrid,c_width,c_height,canvas):
    canvas.delete("all")

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


def recieve_click(event):
     #print((event.x,event.y,window,c_width,c_height,cell_grid))
     global cell_grid,canvas
     handle_click(event.x,event.y,window,c_width,c_height,cell_grid,canvas)
     return event.x,event.y

def handle_click(event_x,event_y,window,canv_x_size,canv_y_size,this_grid,canvas,width=10,height=10):
        x, y = int(event_x // (canv_x_size/width)), int(event_y // (canv_y_size/height))
        if 0 <= x < canv_x_size and 0 <= y < canv_y_size:
            this_grid.grid[x][y] = abs(1 - this_grid.grid[x][y])  # flip the state of the cell
            draw_frame(this_grid,canv_x_size,canv_y_size,canvas)
            window.update()

#setup
window = tk.Tk()
window.geometry("450x450")
window.title("Viewing Window")

#canvas
c_width = 400
c_height = 400
canvas = tk.Canvas(window, width=c_width+1, height=c_height+1, bg="grey")
canvas.bind("<Button-1>",recieve_click)
canvas.pack()

#cell grid
cell_grid = CellGrid()

#pause state
paused = True

#button
def start_thing():
    global paused
    if paused == True:
        paused = False
        pause_cycle()
    elif paused == False:
        window.destroy()

button = tk.Button(window,text="Start/End",command=start_thing)
button.pack()

def pause_cycle():
    global cell_grid, c_width, c_height, canvas
    cell_grid = update_cells(cell_grid,game_of_life_rules)
    draw_frame(cell_grid,c_width,c_height,canvas)
    window.update()
    global paused
    if not paused:
        window.after(200,pause_cycle)

         

#loop
draw_frame(cell_grid,c_width,c_height,canvas)
window.update()
    
#run
window.mainloop()