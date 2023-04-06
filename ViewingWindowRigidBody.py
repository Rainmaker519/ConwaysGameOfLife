import tkinter as tk

#wipes a canvas and draws a new frame with the supplied elements
def draw_frame(elements):
    canvas.delete("all")

    if elements == None:
        return

    for element in elements:
        #create commands take top left and bottom right coordinates
        if element[0] == "rectangle":
            canvas.create_rectangle(element[1], element[2], fill=element[3])
        elif element[0] == "line":
            canvas.create_line(element[1], element[2], fill=element[3])
        elif element[0] == "oval":
            canvas.create_oval(element[1], element[2], fill=element[3])
        elif element[0] == "text":
            canvas.create_text(element[1], element[2], fill=element[3], text=element[4])
        elif element[0] == "image":
            canvas.create_image(element[1], element[2], image=element[3])


#setup
window = tk.Tk()
window.geometry("450x450")
window.title("Viewing Window")

#canvas
canvas = tk.Canvas(window, width=400, height=400, bg="grey")
canvas.pack()

canvas.create_line((0, 0), (200, 200), fill="red")

#run
window.mainloop()