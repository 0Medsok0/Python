import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint App")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.brush_color = "black"
        self.brush_size = 2
        self.brush_type = "circle"  # Default brush type is circle

        self.setup_tools()

        self.canvas.bind("<B1-Motion>", self.paint)

    def setup_tools(self):
        tool_frame = tk.Frame(self.root)
        tool_frame.pack(pady=10)

        color_btn = tk.Button(tool_frame, text="Color", command=self.choose_color)
        color_btn.grid(row=0, column=0, padx=5)

        size_label = tk.Label(tool_frame, text="Brush Size:")
        size_label.grid(row=0, column=1, padx=5)

        self.size_scale = tk.Scale(tool_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_brush_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.grid(row=0, column=2, padx=5)

        brush_label = tk.Label(tool_frame, text="Brush Type:")
        brush_label.grid(row=0, column=3, padx=5)

        self.brush_var = tk.StringVar()
        self.brush_var.set(self.brush_type)

        circle_radio = tk.Radiobutton(tool_frame, text="Circle", variable=self.brush_var, value="circle")
        circle_radio.grid(row=0, column=4, padx=5)

        rectangle_radio = tk.Radiobutton(tool_frame, text="Rectangle", variable=self.brush_var, value="rectangle")
        rectangle_radio.grid(row=0, column=5, padx=5)

        clear_btn = tk.Button(tool_frame, text="Clear", command=self.clear_canvas)
        clear_btn.grid(row=0, column=6, padx=5)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)

        if self.brush_type == "circle":
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)
        elif self.brush_type == "rectangle":
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Brush Color")
        if color[1]:
            self.brush_color = color[1]

    def change_brush_size(self, size):
        self.brush_size = int(size)

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
