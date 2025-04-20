import tkinter as tk

CELL_SIZE = 40
ROWS = 400
COLS = 400
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
        self.canvas.pack()
        self.cells = {}  # Store cell rectangles

        # Draw grid of blue cells
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                self.cells[rect] = (x1, y1, x2, y2)

        # Create eraser rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='white', outline='gray')
        self.canvas.tag_raise(self.eraser)

        # Bind mouse events
        self.canvas.bind('<B1-Motion>', self.move_eraser)

    def move_eraser(self, event):
        # Move eraser to mouse position
        x1 = event.x - ERASER_SIZE // 2
        y1 = event.y - ERASER_SIZE // 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check for overlap with cells
        overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
        for item in overlapping:
            if item in self.cells:
                self.canvas.itemconfig(item, fill='white')

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
